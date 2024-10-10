import pytest
import time
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


def test_google_title(browser):

    # acessa a pagina do google
    browser.goto("https://www.google.com")
    
    # escopo da funcionalidade que será verificada
    titulo_esperado = "Google"
    titulo_obtido   = browser.title()

    # verifica o comportamento
    assert titulo_esperado == titulo_obtido


def test_search_box_visivel(browser):

    # identifica o elemento
    text_area = "textarea[name='q']"
    
    # verifica se o componente está visivel
    esperado = True
    obtido   = browser.is_visible(text_area)

    # o retorno já é um booleano, não precisa comparar com o esperado.
    assert obtido


def test_search_funcionalidade(browser):
    
    # identifica o elemento
    text_area = "textarea[name='q']"

    # realiza as ações sobre o elemento 
    browser.fill(text_area, "Playwright")
    browser.press(text_area, "Enter")
    
    # espera o carregamento da pagina
    time.sleep(3)

    # coleta as informações do teste
    esperado = "Playwright - Pesquisa Google"
    obtido   = browser.title() 

    # verifica o comportamento
    assert esperado == obtido 


def test_images_search_funcionalidade(browser):

    # identifica o link da seção de imagens

    # clica no link (browser.click(link))

    # identifica o textarea de buscar a imagem

    # realiza as ações de inserir texto e enter para buscar

    # espera o processamento da pagina

    # recupera uma informação importante da pagina para realizar o teste

    # realiza o assert para monitorar o comportamento
     
    pass