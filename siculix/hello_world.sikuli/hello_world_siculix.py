# Importa a biblioteca do Sikuli
from sikuli import *

# Abre o Bloco de Notas no Windows
App.open("C:\\Windows\\System32\\notepad.exe")

# Aguarde alguns segundos para o Bloco de Notas abrir
wait(3)

# Espera a janela do Bloco de Notas aparecer
wait("bloco_notas_inicial.png", 10) 

# Escreve "Hello World!"
type("Hello World!")

# Fecha o Bloco de Notas
type(Key.F4, KeyModifier.ALT)

# Abre a calculadora do Windows
App.open("C:\\Windows\\System32\\calc.exe")

# Aguarda alguns segundos até a calculadora abrir
wait(3)

# Espera a calculadora aparecer na tela
wait("calculadora_imagem.png", 10) 

# Realiza a operação 1 + 1
type("1")
type("+")
type("1")
type("=")

# Espera o resultado "2" aparecer na tela
result_found = exists("calculadora_resultado.png", 10)  # Verifica se a imagem do resultado 2 aparece

# Assert para garantir que o resultado 2 foi encontrado
assert result_found, "Erro: O resultado da soma 1 + 1 não é 2 na calculadora."

# Fecha a calculadora
type(Key.F4, KeyModifier.ALT)


# Prática: Abrir o navegador e realizar uma busca no Google

# 1. Abra o navegador
# find("browser_icone.png")  # Localize o ícone do navegador na tela (substitua com a imagem do seu ícone)
# click("browser_icone.png")  # Clique no ícone do navegador

# 2. Aguarde o navegador abrir
# wait("browser_inicial.png", 10)  # Aguarde até que a barra de endereço esteja visível (máximo de 10 segundos)

# 3. Navegue para o Google
# type("https://www.google.com")  # Digite o endereço do Google na barra de endereço
# type(Key.ENTER)  # Pressione 'Enter' para carregar a página

# 4. Aguarde a página carregar
# wait("google_inicial.png", 10)  # Aguarde até o campo de pesquisa aparecer

# 5. Realize uma pesquisa
# type("SikuliX automação")  # Digite o termo de busca no campo de pesquisa
# type(Key.ENTER)  # Pressione 'Enter' para iniciar a busca

# 6. Aguarde os resultados
# wait("resultado_busca.png", 10)  # Aguarde até os resultados da pesquisa aparecerem

#Substitua as imagens (ex: "browser_icon.png") por capturas de tela correspondentes à sua própria interface.







# Funções Comuns do SikuliX:
# 
# 1. Reconhecimento de Imagem:
#    - find(image): Encontra a imagem especificada na tela e retorna sua região.
#    - exists(image): Verifica se a imagem especificada está presente na tela.
#
# 2. Interações com o Mouse:
#    - click(image): Clica na localização da imagem especificada.
#    - doubleClick(image): Dá um duplo clique na localização da imagem.
#    - rightClick(image): Realiza um clique com o botão direito na imagem especificada.
#
# 3. Digitação e Inserção de Texto:
#    - type(text): Digita o texto fornecido no campo que está em foco.
#    - paste(text): Cola o texto fornecido no campo em foco.
#
# 4. Movimentos do Mouse:
#    - hover(image): Move o ponteiro do mouse sobre a imagem especificada.
#    - dragDrop(source, destination): Arrasta da localização de origem para a de destino.
#    - mouseDown() / mouseUp(): Simula pressionar e soltar o botão do mouse.
#
# 5. Captura de Tela:
#    - capture(region): Captura uma imagem da região específica da tela.
#
# 6. Esperar por Condições:
#    - wait(image, timeout): Aguarda até que a imagem apareça na tela dentro do tempo limite.
#    - waitVanish(image, timeout): Aguarda até que a imagem desapareça da tela dentro do tempo limite.
#
# 7. Definindo Regiões da Tela:
#    - Region(): Define uma área específica da tela para procurar imagens.
#    - setROI(x, y, width, height): Define uma região de interesse (ROI) para limitar as buscas de imagem a uma parte específica da tela.
#
# 8. Automação do Teclado:
#    - keyDown(Key): Simula o pressionamento de uma tecla ou combinação de teclas.
#    - keyUp(Key): Simula o soltar de uma tecla.