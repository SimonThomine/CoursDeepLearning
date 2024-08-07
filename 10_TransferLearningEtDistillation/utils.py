import os
import torch
from torch.utils.data import Dataset
import torch.nn.functional as F
from torchvision import transforms as T
import cv2
import numpy as np
import glob
from sklearn.metrics import roc_auc_score
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import matplotlib
from skimage import morphology
from skimage.segmentation import mark_boundaries

class MVTecDataset(Dataset):

    def __init__(self, root_dir, resize_shape=None,crop_size=None,phase="train"):
        self.root_dir = root_dir
        
        image_extensions = ['png', 'tif', 'tiff', 'jpg', 'jpeg']
        pattern = f"{root_dir}/*/*" + '/'.join(f"*.{ext}" for ext in image_extensions)

        self.images = sorted(glob.glob(root_dir+"/*/*.png"))

        self.image_paths = sorted(glob.glob(root_dir+"/*.png"))

        self.resize_shape=resize_shape
        if (crop_size==None):
            crop_size=resize_shape[0]
        self.transform=T.Compose([T.CenterCrop(crop_size)]) #,T.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])
        self.phase=phase
        
    def __len__(self):
        if self.phase=="test":
            return len(self.images)
        else:
            return len(self.image_paths)

    def transform_image(self, image_path):
        
        
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        
        if self.resize_shape != None:
            image = cv2.resize(image, dsize=(self.resize_shape[1], self.resize_shape[0]))
            
        image = np.array(image).reshape((image.shape[0], image.shape[1], 3)).astype(np.float32)/ 255.0
        
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = np.transpose(image, (2, 0, 1))
        image=np.asarray(self.transform(torch.from_numpy(image)))
      
        return image

 
    def __getitem__(self, idx):
        if self.phase=="test":
            if torch.is_tensor(idx):
                idx = idx.tolist()
            img_path = self.images[idx]
            dir_path, file_name = os.path.split(img_path)
            base_dir = os.path.basename(dir_path)
            image = self.transform_image(img_path)
            if base_dir == 'good':
                has_anomaly = np.array([0], dtype=np.int64)
            else:
                has_anomaly = np.array([1], dtype=np.int64)
            sample = {'imageBase': image, 'has_anomaly': has_anomaly, 'idx': idx}
        else:
            idx = torch.randint(0, len(self.image_paths), (1,)).item()
            image = self.transform_image(self.image_paths[idx])
            sample = {'imageBase': image}
        return sample

def computeAUROC(scores,gt_list,obj,name="base"):
  max_anomaly_score = scores.max()
  min_anomaly_score = scores.min()
  scores = (scores - min_anomaly_score) / (max_anomaly_score - min_anomaly_score)
  img_scores = scores.reshape(scores.shape[0], -1).max(axis=1)
  img_roc_auc = roc_auc_score(gt_list, img_scores)
  print(obj + " image"+str(name)+" ROCAUC: %.3f" % (img_roc_auc))
  return img_roc_auc,img_scores 


@torch.no_grad()
def cal_anomaly_maps(fs_list, ft_list, out_size):
  anomaly_map = 0
  for i in range(len(ft_list)):
    fs = fs_list[i]
    ft = ft_list[i]
    fs_norm = F.normalize(fs, p=2)
    ft_norm = F.normalize(ft, p=2)

    _, _, h, w = fs.shape

    a_map = (0.5 * (ft_norm - fs_norm) ** 2) / (h * w)

    a_map = a_map.sum(1, keepdim=True)

    a_map = F.interpolate(
        a_map, size=out_size, mode="bilinear", align_corners=False
    )
    anomaly_map += a_map
  anomaly_map = anomaly_map.squeeze().cpu().numpy()
  for i in range(anomaly_map.shape[0]):
    anomaly_map[i] = gaussian_filter(anomaly_map[i], sigma=4)

  return anomaly_map


def plt_fig(
    test_img, scores, img_scores, gts, threshold, cls_threshold, save_dir, class_name
):
    num = len(scores)
    vmax = scores.max() * 255.0
    vmin = scores.min() * 255.0
    vmax = vmax * 0.5 + vmin * 0.5
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)
    for i in range(num):
        img = test_img[i]
        gt = gts[i].squeeze()
        heat_map = scores[i] * 255
        mask = scores[i]
        mask[mask > threshold] = 1
        mask[mask <= threshold] = 0
        kernel = morphology.disk(4)
        mask = morphology.opening(mask, kernel)
        mask *= 255
        vis_img = mark_boundaries(img, mask, color=(1, 0, 0), mode="thick")
        fig_img, ax_img = plt.subplots(
            1, 4, figsize=(9, 3), gridspec_kw={"width_ratios": [4, 4, 4, 3]}
        )

        fig_img.subplots_adjust(wspace=0.05, hspace=0)
        for ax_i in ax_img:
            ax_i.axes.xaxis.set_visible(False)
            ax_i.axes.yaxis.set_visible(False)

        ax_img[0].imshow(img)
        ax_img[0].title.set_text("Input image")
        ax_img[1].imshow(gt, cmap="gray")
        ax_img[1].title.set_text("GroundTruth")
        ax_img[2].imshow(heat_map, cmap="jet", norm=norm, interpolation="none")
        # ax_img[2].imshow(vis_img, cmap='gray', alpha=0.7, interpolation='none')
        ax_img[2].imshow(img, cmap="gray", alpha=0.7, interpolation="none")
        ax_img[2].title.set_text("Segmentation")
        black_mask = np.zeros((int(mask.shape[0]), int(3 * mask.shape[1] / 4)))
        ax_img[3].imshow(black_mask, cmap="gray")
        ax = plt.gca()
        if img_scores[i] > cls_threshold:
            cls_result = "nok"
        else:
            cls_result = "ok"

        ax.text(
            0.05,
            0.89,
            "Detected anomalies",
            verticalalignment="bottom",
            horizontalalignment="left",
            transform=ax.transAxes,
            fontdict=dict(
                fontsize=8,
                color="w",
                family="sans-serif",
            ),
        )
        ax.text(
            0.05,
            0.79,
            "------------------------",
            verticalalignment="bottom",
            horizontalalignment="left",
            transform=ax.transAxes,
            fontdict=dict(
                fontsize=8,
                color="w",
                family="sans-serif",
            ),
        )
        ax.text(
            0.05,
            0.72,
            "Results",
            verticalalignment="bottom",
            horizontalalignment="left",
            transform=ax.transAxes,
            fontdict=dict(
                fontsize=8,
                color="w",
                family="sans-serif",
            ),
        )
        ax.text(
            0.05,
            0.67,
            "------------------------",
            verticalalignment="bottom",
            horizontalalignment="left",
            transform=ax.transAxes,
            fontdict=dict(
                fontsize=8,
                color="w",
                family="sans-serif",
            ),
        )
        ax.text(
            0.05,
            0.59,
            "'{}'".format(cls_result),
            verticalalignment="bottom",
            horizontalalignment="left",
            transform=ax.transAxes,
            fontdict=dict(
                fontsize=8,
                color="r",
                family="sans-serif",
            ),
        )
        ax.text(
            0.05,
            0.47,
            "Anomaly scores: {:.2f}".format(img_scores[i]),
            verticalalignment="bottom",
            horizontalalignment="left",
            transform=ax.transAxes,
            fontdict=dict(
                fontsize=8,
                color="w",
                family="sans-serif",
            ),
        )
        ax.text(
            0.05,
            0.37,
            "------------------------",
            verticalalignment="bottom",
            horizontalalignment="left",
            transform=ax.transAxes,
            fontdict=dict(
                fontsize=8,
                color="w",
                family="sans-serif",
            ),
        )
        ax.text(
            0.05,
            0.30,
            "Thresholds",
            verticalalignment="bottom",
            horizontalalignment="left",
            transform=ax.transAxes,
            fontdict=dict(
                fontsize=8,
                color="w",
                family="sans-serif",
            ),
        )
        ax.text(
            0.05,
            0.25,
            "------------------------",
            verticalalignment="bottom",
            horizontalalignment="left",
            transform=ax.transAxes,
            fontdict=dict(
                fontsize=8,
                color="w",
                family="sans-serif",
            ),
        )
        ax.text(
            0.05,
            0.17,
            "Classification: {:.2f}".format(cls_threshold),
            verticalalignment="bottom",
            horizontalalignment="left",
            transform=ax.transAxes,
            fontdict=dict(
                fontsize=8,
                color="w",
                family="sans-serif",
            ),
        )
        ax.text(
            0.05,
            0.07,
            "Segmentation: {:.2f}".format(threshold),
            verticalalignment="bottom",
            horizontalalignment="left",
            transform=ax.transAxes,
            fontdict=dict(
                fontsize=8,
                color="w",
                family="sans-serif",
            ),
        )
        ax_img[3].title.set_text("Classification")
        plt.show()
        # fig_img.savefig(
        #     os.path.join(save_dir, class_name + "_{}".format(i)),
        #     dpi=300,
        #     bbox_inches="tight",
        # )
        plt.close()