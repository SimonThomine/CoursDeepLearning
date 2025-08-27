#!/usr/bin/env python3
"""
Build script for multilingual Jupyter Book
"""

import os
import shutil

import subprocess
import sys
from pathlib import Path


def copy_standalone_qcms(lang, build_dir):
    """Copy standalone QCM files to the build directory"""
    print(f"📋 Copie des QCM standalone pour {lang}...")

    source_lang_dir = Path(lang)
    target_html_dir = Path(f"{build_dir}/_build/html")

    if not target_html_dir.exists():
        print(f"⚠️ Répertoire de build {target_html_dir} introuvable")
        return False

    copied_count = 0

    # Parcourir tous les dossiers de chapitres dans la langue
    for chapter_dir in source_lang_dir.iterdir():
        if chapter_dir.is_dir():
            # Chercher les fichiers QCM standalone
            qcm_files = list(chapter_dir.glob("*qcm*.html"))

            for qcm_file in qcm_files:
                # Éviter de copier les fichiers générés par Sphinx
                if "standalone" in qcm_file.name or not any(x in qcm_file.name for x in ["_build", "doctrees"]):

                    # Créer le répertoire de destination
                    target_chapter_dir = target_html_dir / chapter_dir.name
                    target_chapter_dir.mkdir(parents=True, exist_ok=True)

                    # Copier le fichier
                    target_file = target_chapter_dir / qcm_file.name
                    try:
                        shutil.copy2(qcm_file, target_file)
                        print(f"  ✅ Copié: {qcm_file} → {target_file}")
                        copied_count += 1
                    except Exception as e:
                        print(
                            f"  ❌ Erreur lors de la copie de {qcm_file}: {e}")

    if copied_count > 0:
        print(f"📋 {copied_count} fichier(s) QCM copiés pour {lang}")
    else:
        print(f"📋 Aucun QCM standalone trouvé pour {lang}")

    return True


def run_command(cmd, cwd=None):
    """Run a command and return the result"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd,
                            capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    print(f"Success: {result.stdout}")
    return True


def build_language_version(lang_dir, output_dir):
    """Build a specific language version"""
    print(f"\n🔨 Building {lang_dir} version...")

    # Change to language directory
    os.chdir(lang_dir)

    # Build the book
    cmd = f"jupyter-book build . --path-output ../{output_dir}"
    success = run_command(cmd)

    # Return to parent directory
    os.chdir("..")

    # Copy language switcher JavaScript to build directory
    if success and Path(f"{output_dir}/_build/html").exists():
        import shutil
        js_source = "language-switcher.js"
        js_dest = f"{output_dir}/_build/html/language-switcher.js"
        if Path(js_source).exists():
            shutil.copy2(js_source, js_dest)
            print(f"📄 Copied language switcher to {js_dest}")
        # Copy standalone QCM files
        copy_standalone_qcms(lang_dir, output_dir)
    return success


def main():
    """Main build function"""
    print("🚀 Building Multilingual Jupyter Book")

    # Ensure we're in the right directory
    for lang in ["fr", "en", "es", "zh"]:
        if not Path(lang).exists():
            print(f"Error: {lang}/ directory not found!")
            sys.exit(1)

    # Build each language version
    for lang, build_dir in [("fr", "_build_fr"), ("en", "_build_en"), ("es", "_build_es"), ("zh", "_build_zh")]:
        if not build_language_version(lang, build_dir):
            print(f"❌ Failed to build {lang} version")
            sys.exit(1)

    print("\n✅ Successfully built all language versions!")
    print("📁 French version: _build_fr/_build/html/")
    print("📁 English version: _build_en/_build/html/")
    print("📁 Spanish version: _build_es/_build/html/")
    print("📁 Chinese version: _build_zh/_build/html/")

    # Create index page for language selection
    create_language_selector()


def create_language_selector():
    """Create a main index page for language selection"""
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deep Learning Course / Cours Deep Learning</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 50%, #95a5a6 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            animation: gradientShift 10s ease infinite;
            background-size: 400% 400%;
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        .container {
            text-align: center;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            padding: 4rem 3rem;
            border-radius: 30px;
            box-shadow: 0 30px 60px rgba(0,0,0,0.15);
            max-width: 900px;
            width: 100%;
            border: 1px solid rgba(255, 255, 255, 0.3);
            transform: translateY(0);
            transition: transform 0.3s ease;
        }
        
        .container:hover {
            transform: translateY(-5px);
        }
        
        .header {
            margin-bottom: 3rem;
        }
        
        h1 {
            color: #2d3748;
            margin-bottom: 1rem;
            font-size: clamp(2rem, 4vw, 3rem);
            font-weight: 700;
            background: linear-gradient(135deg, #2c3e50, #34495e, #95a5a6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .subtitle {
            color: #4a5568;
            font-size: 1.3rem;
            font-weight: 400;
            margin-bottom: 0.5rem;
        }
        
        .description {
            color: #718096;
            font-size: 1rem;
            font-style: italic;
        }
        
        .language-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1.5rem;
            margin: 3rem 0;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .lang-card {
            display: block;
            text-decoration: none;
            padding: 2rem 1.5rem;
            border-radius: 20px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
            border: 2px solid transparent;
            background: white;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .lang-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            opacity: 0;
            transition: opacity 0.3s ease;
            border-radius: 18px;
        }
        
        .lang-card.french::before {
            background: linear-gradient(135deg, #0055A4, #EF4135);
        }
        
        .lang-card.english::before {
            background: linear-gradient(135deg, #012169, #C8102E);
        }
        
        .lang-card.spanish::before {
            background: linear-gradient(135deg, #C60B1E, #FFC400);
        }
        
        .lang-card.chinese::before {
            background: linear-gradient(135deg, #DE2910, #FFDE00);
        }
        
        .lang-card:hover::before {
            opacity: 0.1;
        }
        
        .lang-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            border-color: rgba(102, 126, 234, 0.3);
        }
        
        .flag {
            font-size: 3rem;
            margin-bottom: 1rem;
            display: block;
            filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));
        }
        
        .lang-name {
            font-size: 1.5rem;
            font-weight: 700;
            color: #2d3748;
            margin-bottom: 0.5rem;
            position: relative;
            z-index: 1;
        }
        
        .lang-subtitle {
            font-size: 0.95rem;
            color: #718096;
            font-weight: 400;
            position: relative;
            z-index: 1;
        }
        
        .status-badge {
            position: absolute;
            top: 15px;
            right: 15px;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        .available {
            background: #48bb78;
            color: white;
        }
        
        .coming-soon {
            background: #ed8936;
            color: white;
        }
        
        .footer {
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #e2e8f0;
        }
        
        .footer-text {
            color: #718096;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        
        .github-link {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s ease;
        }
        
        .github-link:hover {
            color: #5a67d8;
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 2rem 1.5rem;
                margin: 10px;
            }
            
            .language-grid {
                grid-template-columns: 1fr;
                gap: 1.5rem;
            }
            
            .lang-card {
                padding: 1.5rem 1rem;
            }
        }
        
        @media (max-width: 480px) {
            .language-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 AI Course</h1>
            <p class="subtitle">Interactive Deep Learning Tutorial</p>
        </div>
        
        <div class="language-grid">
            <a href="fr/index.html" class="lang-card french">
                <span class="status-badge available">Disponible</span>
                <span class="flag">🇫🇷</span>
                <div class="lang-name">Français</div>
                <div class="lang-subtitle">Version française complète</div>
            </a>
            
            <a href="en/index.html" class="lang-card english">
                <span class="status-badge available">Available</span>
                <span class="flag">🇺🇸</span>
                <div class="lang-name">English</div>
                <div class="lang-subtitle">Complete English version</div>
            </a>
            
            <a href="es/index.html" class="lang-card spanish">
                <span class="status-badge available">Disponible</span>
                <span class="flag">🇪🇸</span>
                <div class="lang-name">Español</div>
                <div class="lang-subtitle">Versión completa en español</div>
            </a>
            
            <a href="zh/index.html" class="lang-card chinese">
                <span class="status-badge available">可用</span>
                <span class="flag">🇨🇳</span>
                <div class="lang-name">中文</div>
                <div class="lang-subtitle">完整中文版</div>
            </a>
        </div>
        
        <div class="footer">
            <p class="footer-text">
                Created with ❤️ by Simon Thomine
            </p>
            <p class="footer-text">
                <a href="https://github.com/SimonThomine/CoursDeepLearning" class="github-link">
                    📚 View on GitHub
                </a>
            </p>
        </div>
    </div>
</body>
</html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("📄 Created beautiful language selector: index.html")


if __name__ == "__main__":
    main()
