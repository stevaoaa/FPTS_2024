from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

import time

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = '4723'

def test_calculator():
    # Iniciando o serviço Appium
    service = AppiumService()
    service.start(args=['--address', DEFAULT_HOST, '-p', str(DEFAULT_PORT)])

    print("INFO: Iniciando o serviço Appium")

    if service.is_running:
        print("INFO: Appium está em execução.")
        
        # Criando uma instância de UiAutomator2Options com as capabilities do meu celular (varia de acordo com o modelo)
        options = UiAutomator2Options()
        options.set_capability("platformName", "Android")
        options.set_capability("platformVersion", "14.0")
        options.set_capability("deviceName", "RXCWB05ZRQL")
        options.set_capability("automationName", "UiAutomator2")
        options.set_capability("app", "C:\\Users\\stevao\\Desktop\\curso teste\\Fundamentos e práticas do teste de software\\appium\\calculator-7-8-271241277.apk")
        options.set_capability("noReset", True)
        options.set_capability("fullReset", False)

        # Inicializando o driver do Appium
        driver = webdriver.Remote(f'http://{DEFAULT_HOST}:{DEFAULT_PORT}', options=options)
        
        print("INFO: Driver iniciado com sucesso.")

        # Testando a calculadora: 1 + 1 = 2
        driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_1").click()
        driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_add").click()
        driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_1").click()
        driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq").click()

        # Aguardando para capturar o resultado
        time.sleep(2)

        # Capturando o resultado
        result = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final").text

        # realizando o teste
        assert result == "2", f"Resultado incorreto: {result}"

        print(f"INFO: O resultado da operação foi {result}.")
        
        # Fechando o driver
        driver.quit()

    else:
        print("ERRO: O serviço Appium não foi iniciado corretamente.")
    
    # Encerrando o serviço Appium
    service.stop()
    print("INFO: Serviço Appium encerrado.")