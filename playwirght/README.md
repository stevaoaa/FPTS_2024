# Teste Automatizado com Playwright e Pytest

Este projeto demonstra como usar o Playwright junto com o framework de testes `pytest` para automatizar o teste de uma página web. O teste navega até `https://google.com` e faz um `assert` sobre o título da página.

## Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.7+).

Você também precisará instalar o Playwright, o pytest e os navegadores necessários.

## Instalação

1. Clone este repositório ou faça o download dos arquivos.

2. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências listadas no arquivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. Instale os navegadores para o Playwright:

   ```bash
   playwright install
   ```

## Executando o projeto

Para rodar os testes usando o pytest, execute o comando abaixo:

```bash
pytest
```

O pytest encontrará o arquivo `test_playwright_hello_world.py`, abrirá o navegador, navegará até a página `https://google.com`, verificará se o título está correto e fechará o navegador.

## Modo headless

Se você quiser executar o teste no modo headless, basta alterar o valor de `headless` para `True` na linha:

```python
browser = playwright_instance.chromium.launch(headless=True)
```

Isso permite que o teste seja executado sem abrir a interface gráfica do navegador, útil para integrações contínuas (CI/CD).
```