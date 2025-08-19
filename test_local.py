#!/usr/bin/env python3
"""
Script de test local pour vérifier le changement de langue
"""

import webbrowser
import http.server
import socketserver
import threading
import time
import os
from pathlib import Path


def start_server(port=8000):
    """Démarre un serveur HTTP local"""
    os.chdir(Path(__file__).parent)

    class Handler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            # Supprime les logs du serveur pour plus de clarté
            pass

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"🌐 Serveur démarré sur http://localhost:{port}")
        httpd.serve_forever()


def main():
    """Fonction principale"""
    print("🚀 Test local du Jupyter Book multilingue")
    print("=" * 50)

    # Vérifier que les builds existent
    if not Path("_build_fr/_build/html/index.html").exists():
        print("❌ Build français non trouvé. Exécutez d'abord:")
        print("   python build_multilingual.py")
        return

    if not Path("_build_en/_build/html/index.html").exists():
        print("❌ Build anglais non trouvé. Exécutez d'abord:")
        print("   python build_multilingual.py")
        return

    print("✅ Builds trouvés")

    # Démarrer le serveur dans un thread séparé
    port = 8000
    server_thread = threading.Thread(
        target=start_server, args=(port,), daemon=True)
    server_thread.start()

    # Attendre que le serveur démarre
    time.sleep(1)

    # URLs de test
    base_url = f"http://localhost:{port}"
    test_urls = {
        "Sélecteur de langue": f"{base_url}/index.html",
        "Page de test": f"{base_url}/test_switching.html",
        "Version française": f"{base_url}/_build_fr/_build/html/index.html",
        "Version anglaise": f"{base_url}/_build_en/_build/html/index.html",
    }

    print(f"\n📋 URLs de test disponibles:")
    for name, url in test_urls.items():
        print(f"   {name}: {url}")

    print(f"\n🧪 Instructions de test:")
    print("1. Le navigateur va s'ouvrir avec le sélecteur de langue")
    print("2. Choisissez une langue pour accéder au livre")
    print("3. Naviguez vers une page du cours")
    print("4. Utilisez les boutons de langue dans le footer")
    print("5. Vérifiez que le changement fonctionne")

    print(f"\n⚠️  Note: Gardez ce terminal ouvert (serveur actif)")
    print("   Appuyez sur Ctrl+C pour arrêter le serveur")

    # Ouvrir le navigateur
    webbrowser.open(test_urls["Sélecteur de langue"])

    try:
        # Garder le script actif
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n🛑 Serveur arrêté")


if __name__ == "__main__":
    main()
