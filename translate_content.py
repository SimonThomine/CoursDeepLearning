#!/usr/bin/env python3
"""
Helper script for translating content between French and English versions
"""

import os
import json
import re
from pathlib import Path


def extract_notebook_text(notebook_path):
    """Extract text content from a Jupyter notebook"""
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    text_content = []
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            source = cell.get('source', [])
            if isinstance(source, list):
                text_content.append(''.join(source))
            else:
                text_content.append(source)

    return text_content


def create_translation_template(fr_path, en_path):
    """Create English template from French content"""
    fr_notebooks = list(Path(fr_path).rglob('*.ipynb'))

    for fr_notebook in fr_notebooks:
        # Calculate corresponding English path
        rel_path = fr_notebook.relative_to(fr_path)
        en_notebook = Path(en_path) / rel_path

        # Create directory if it doesn't exist
        en_notebook.parent.mkdir(parents=True, exist_ok=True)

        # Skip if English version already exists
        if en_notebook.exists():
            continue

        print(f"Creating template: {en_notebook}")

        # Load French notebook
        with open(fr_notebook, 'r', encoding='utf-8') as f:
            notebook = json.load(f)

        # Create English template with translation placeholders
        for cell in notebook.get('cells', []):
            if cell.get('cell_type') == 'markdown':
                source = cell.get('source', [])
                if isinstance(source, list):
                    # Add translation comment
                    cell['source'] = [
                        '<!-- TODO: Translate from French -->\n'] + source
                else:
                    cell['source'] = '<!-- TODO: Translate from French -->\n' + source

        # Save English template
        with open(en_notebook, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=2, ensure_ascii=False)


def translate_titles():
    """Dictionary of common translations for titles and headers"""
    translations = {
        # Course sections
        "Fondations": "Foundations",
        "Réseau Fully Connected": "Fully Connected Networks",
        "Réseau Convolutifs": "Convolutional Networks",
        "Autoencodeurs": "Autoencoders",
        "Entrainement Contrastif": "Contrastive Training",
        "Transfer Learning Et Distillation": "Transfer Learning and Distillation",
        "Modeles Generatifs": "Generative Models",
        "Detection Et Yolo": "Detection and YOLO",
        "Bonus Cours Spécifiques": "Bonus Specific Topics",

        # Common terms
        "Introduction": "Introduction",
        "Implémentation": "Implementation",
        "Application": "Application",
        "Techniques Avancées": "Advanced Techniques",
        "Mon Premier Réseau": "My First Network",
        "Couches de Convolutions": "Convolutional Layers",
        "Réseau Convolutif": "Convolutional Network",
        "Classification": "Classification",
        "Segmentation": "Segmentation",
        "Intuition et Premier AE": "Intuition and First AE",
        "Denoising AE": "Denoising AE",
        "Réseaux Fully Connected": "Fully Connected Networks",
        "Rnn": "RNN",
        "Lstm": "LSTM",
        "Computer Vision With Transformers": "Computer Vision With Transformers",
        "NLP With Transformers": "NLP With Transformers",
        "Audio With Transformers": "Audio With Transformers",
        "Image Generation With Diffusers": "Image Generation With Diffusers",
        "Demo Avec Gradio": "Demo With Gradio",
        "GPT From Scratch": "GPT From Scratch",
        "Training Our GPT": "Training Our GPT",
        "Architecture Et Particularités": "Architecture and Specificities",
        "Utilisations Possibles": "Possible Uses",
        "Vision Transformer Implementation": "Vision Transformer Implementation",
        "Swin Transformer": "Swin Transformer",
        "YOLO En Detail": "YOLO In Detail",
        "Face Verification": "Face Verification",
        "Non Supervisé": "Unsupervised",
        "Transfer Learning Pytorch": "Transfer Learning PyTorch",
        "Distillation": "Distillation",
        "Distillation Anomalie": "Anomaly Distillation",
        "Fine Tuning LLM": "Fine Tuning LLM",
        "Fine Tuning Bert HF": "Fine Tuning Bert HF",
        "GAN Implementation": "GAN Implementation",
        "VAE Implementation": "VAE Implementation",
        "Normalizing Flows": "Normalizing Flows",
        "Diffusion Models": "Diffusion Models",
        "Diffusion Implementation": "Diffusion Implementation",
        "Activation Et Initialisation": "Activation and Initialization",
        "Batch Norm": "Batch Norm",
        "Data Augmentation": "Data Augmentation",
        "Broadcasting": "Broadcasting",
        "Optimizer": "Optimizer",
        "Regularisation": "Regularization",
        "Connexions Residuelles": "Residual Connections",
        "Cross Validation": "Cross Validation",
        "Metriques Evaluation": "Evaluation Metrics",
        "Tokenization": "Tokenization",
        "Quantization": "Quantization"
    }

    return translations


def main():
    """Main function"""
    print("🔄 Content Translation Helper")

    fr_path = Path("fr")
    en_path = Path("en")

    if not fr_path.exists():
        print("❌ French content directory 'fr/' not found!")
        return

    # Create English directory if it doesn't exist
    en_path.mkdir(exist_ok=True)

    # Create translation templates
    print("📝 Creating English templates from French content...")
    create_translation_template(fr_path, en_path)

    print("✅ Translation templates created!")
    print("📋 Next steps:")
    print("1. Review the generated English files in en/ directory")
    print("2. Translate the markdown content manually")
    print("3. Update the table of contents in en/_toc.yml")
    print("4. Build and test with: python build_multilingual.py")


if __name__ == "__main__":
    main()
