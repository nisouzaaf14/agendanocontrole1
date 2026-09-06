# Agenda Cheia no WhatsApp — Página de Vendas

Landing page (site estático, um único `index.html`) do produto **Método C.A.S.A. — Agenda Cheia no WhatsApp**, para nail designers.

## Estrutura

```
.
├── index.html        # página completa (HTML + CSS + JS inline)
├── server.py         # script Python para rodar a página localmente
└── assets/
    ├── capa-agenda-no-controle.jpg
    ├── preview-biblioteca-mensagens.jpg
    ├── preview-kit-antifuro.jpg
    └── preview-nailgpt.jpg
```

As imagens usam caminho relativo (`assets/...`), então **a pasta `assets` precisa continuar ao lado do `index.html`** — não mova ou renomeie um sem o outro.

## Rodar localmente (Python)

Sem instalar nada além do Python 3 (já vem pronto no Windows, Mac e Linux):

```bash
python3 server.py
```

Isso abre automaticamente `http://localhost:8000` no navegador, servindo o `index.html` e a pasta `assets` exatamente como um site real. Para usar outra porta:

```bash
python3 server.py 5000
```

Isso é só para visualizar/testar antes de publicar — para o site ficar no ar, use o GitHub Pages abaixo.

## Publicar com GitHub Pages

1. Suba este repositório para o GitHub.
2. Vá em **Settings → Pages**.
3. Em "Branch", selecione a branch principal (ex.: `main`) e a pasta `/ (root)`.
4. Salve — o GitHub gera uma URL do tipo `https://seu-usuario.github.io/nome-do-repo/`.

## Antes de divulgar

- Troque a URL de checkout em `CONFIG.checkoutUrl` (dentro do `<script>`, no final do `index.html`) pelo link real de pagamento.
- Troque `COLOQUE_AQUI_A_URL_DE_CHECKOUT` no JSON-LD (`<script type="application/ld+json">`) pela mesma URL de checkout.
- Troque `href="https://www.seudominio.com.br/..."` (canonical, `og:image`, `twitter:image`) pela URL final publicada — o WhatsApp e as redes sociais só geram preview de link a partir de uma URL `https://` real, hospedada (ex.: a própria URL do GitHub Pages + `/assets/capa-agenda-no-controle.jpg`).
- Confira se o preço (atualmente **R$ 17,90**) está igual nos três lugares: texto da oferta, `CONFIG.price` no `<script>` e `"price"` no JSON-LD.

## Sobre as imagens

As capturas em `assets/` foram extraídas do PDF do material (capa, uma página de exemplo da biblioteca de mensagens, o Kit Anti-Furo & Reativação e o bônus NailGPT) e usadas na seção "Dê uma olhada por dentro".
