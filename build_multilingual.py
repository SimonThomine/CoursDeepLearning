#!/usr/bin/env python3
"""
Build script for multilingual Jupyter Book
"""

import os
import subprocess
import sys
from pathlib import Path


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

    return success


def main():
    """Main build function"""
    print("🚀 Building Multilingual Jupyter Book")

    # Ensure we're in the right directory
    if not Path("fr").exists() or not Path("en").exists():
        print("Error: fr/ and en/ directories not found!")
        sys.exit(1)

    # Build French version
    if not build_language_version("fr", "_build_fr"):
        print("❌ Failed to build French version")
        sys.exit(1)

    # Build English version
    if not build_language_version("en", "_build_en"):
        print("❌ Failed to build English version")
        sys.exit(1)

    print("\n✅ Successfully built both language versions!")
    print("📁 French version: _build_fr/_build/html/")
    print("📁 English version: _build_en/_build/html/")

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
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            text-align: center;
            background: white;
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            max-width: 600px;
        }
        h1 {
            color: #333;
            margin-bottom: 2rem;
            font-size: 2.5rem;
        }
        .language-buttons {
            display: flex;
            gap: 2rem;
            justify-content: center;
            margin-top: 2rem;
        }
        .lang-btn {
            display: block;
            padding: 1.5rem 2rem;
            text-decoration: none;
            border-radius: 15px;
            font-size: 1.2rem;
            font-weight: 600;
            transition: all 0.3s ease;
            min-width: 200px;
        }
        .lang-btn.french {
            background: linear-gradient(45deg, #0055A4, #EF4135, #FFFFFF);
            color: white;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
        }
        .lang-btn.english {
            background: linear-gradient(45deg, #012169, #FFFFFF, #C8102E);
            color: #012169;
            font-weight: bold;
        }
        .lang-btn:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }
        .description {
            color: #666;
            margin: 1rem 0;
            font-size: 1.1rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Deep Learning Course</h1>
        <p class="description">
            Choose your language / Choisissez votre langue
        </p>
        
        <div class="language-buttons">
            <a href="_build_fr/_build/html/index.html" class="lang-btn french">
                🇫🇷 Français<br>
                <small>Version Française</small>
            </a>
            <a href="_build_en/_build/html/index.html" class="lang-btn english">
                🇺🇸 English<br>
                <small>English Version</small>
            </a>
        </div>
        
        <p style="margin-top: 2rem; color: #888; font-size: 0.9rem;">
            By Simon Thomine | 
            <a href="https://github.com/SimonThomine/CoursDeepLearning" style="color: #667eea;">GitHub</a>
        </p>
    </div>
</body>
</html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("📄 Created language selector: index.html")


if __name__ == "__main__":
    main()
