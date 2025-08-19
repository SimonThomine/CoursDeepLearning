import cv2
import numpy as np
import matplotlib.pyplot as plt

def draw_box(image,output):
    cv_image = np.array(image)
    for bbox in output:
        box = bbox['box']
        label = bbox['label']
        cv2.rectangle(cv_image, (box['xmin'], box['ymin']), (box['xmax'], box['ymax']), (0, 0, 255), 2)
        cv2.putText(cv_image, label, (box['xmin'], box['ymin'] - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        return cv_image

def draw_masks(image,masks):
    image_np = np.array(image)
    colors = plt.cm.get_cmap('tab20', 38)
    for i, mask in enumerate(masks):
        color = colors(i)[:3] 
        color = tuple(int(c * 255) for c in color)  

        image_np[mask] = image_np[mask] * 0.5 + np.array(color) * 0.5
        
    return image_np