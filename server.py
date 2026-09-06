#!/usr/bin/env python3
"""
Servidor local simples para a página "Agenda Cheia no WhatsApp".

Uso:
    python3 server.py            # sobe em http://localhost:8000
    python3 server.py 5000       # sobe em outra porta, ex: 5000

Ele apenas serve os arquivos desta pasta (index.html + assets/) como um
site estático, igual a hospedagem final vai fazer — não precisa instalar
nada além do Python (usa só a biblioteca padrão).
"""

import http.server
import os
import sys
import webbrowser

PASTA_DO_SITE = os.path.dirname(os.path.abspath(__file__))
PORTA_PADRAO = 8000


def main():
    porta = int(sys.argv[1]) if len(sys.argv) > 1 else PORTA_PADRAO
    os.chdir(PASTA_DO_SITE)

    handler = http.server.SimpleHTTPRequestHandler
    with http.server.ThreadingHTTPServer(("localhost", porta), handler) as servidor:
        url = f"http://localhost:{porta}/index.html"
        print(f"Servindo {PASTA_DO_SITE}")
        print(f"Abra no navegador: {url}")
        print("Pressione Ctrl+C para parar.")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            servidor.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor encerrado.")


if __name__ == "__main__":
    main()
