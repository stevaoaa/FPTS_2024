# Hello World com Appium e Python

Este projeto demonstra como usar o Appium com Python para interagir com um aplicativo Android nativo. O exemplo realiza uma operação de soma simples no aplicativo de calculadora Android.

## Pré-requisitos

1. **Appium Server**: Você precisa ter o Appium Server instalado e rodando. Pode ser instalado via npm:
   ```bash
   npm install -g appium
   appium
   ```

2. **Android SDK**: Certifique-se de ter o SDK do Android instalado e configurado. Configure também o emulador ou dispositivo físico conectado via USB.

3. **Python**: Certifique-se de ter o Python instalado (versão 3.7+).

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

## Executando o projeto

1. Certifique-se de que o **Appium Server** está rodando:

   ```bash
   appium
   ```

2. Certifique-se de que um **emulador Android** ou um **dispositivo Android** está conectado.

3. Baixe o APK da calculadora e mova para a raiz do projeto

- https://google-inc-calculator.br.uptodown.com/android/download

4. Execute o teste com o pytest:

   ```bash
   pytest
   ```

O pytest irá rodar o script `test_hello_world.py`, abrir o aplicativo de calculadora Android, realizar a soma `1 + 1` e verificar se o resultado é `2`.

## Personalizações

- Se você estiver usando uma versão diferente do Android, altere `"platformVersion"` para a versão correta no arquivo `test_appium_hello_world.py`.
- Se estiver usando um dispositivo físico, altere `"deviceName"` para o nome correto do dispositivo ou emulador.