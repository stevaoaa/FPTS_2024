# Hello World com SikuliX e Python

Este projeto demonstra como usar o SikuliX para automatizar a interação com uma interface gráfica. O exemplo abre o bloco de notas no Windows, escreve "Hello World" e fecha a aplicação.

## Pré-requisitos

1. **SikuliX**: Você precisa ter o SikuliX configurado. Siga o passo a passo para instalação [aqui](https://sikulix.github.io/docs).

2. **Java**: Certifique-se de que o Java 8 ou superior está instalado em sua máquina.

## Instalação

1. Baixe o SikuliX [aqui](https://sikulix.github.io/docs/download.html). Isso inclui o IDE do SikuliX para criação e execução de scripts.

2. No diretório que contém o JAR baixado, execute o comando abaixo para iniciar o Sikulix (observar a versão no nome do arquivo e ajustar de acordo com o arquivo baixado):

   ```bash
   java -jar .\sikulixide-2.0.5.jar
   ```

3. Crie um novo projeto ou abra o projeto fornecido (`hello_world.sikuli/`), que contém o arquivo `hello_world.py`.

4. Abra o script no IDE do SikuliX e ajuste as imagens, se necessário. Para o exemplo, você precisará de uma captura da janela do bloco de notas (`notepad_janela.png`), que pode ser feita diretamente na IDE.

## Executando o Projeto

1. Abra o **SikuliX IDE**.

2. Abra a pasta `hello_world.sikuli` no IDE.

3. Execute o script diretamente no SikuliX IDE.

O SikuliX abrirá o bloco de notas, escreverá "Hello World" e fechará o aplicativo automaticamente.

## Personalizações

- Se você estiver em um sistema diferente (como Linux ou macOS), ajuste o comando `App.open("notepad.exe")` para abrir o editor de texto do seu sistema (ex.: `gedit`, `nano`, etc.).
- Se necessário, atualize a captura de tela (`notepad_janela.png`) com a interface correta do seu sistema.