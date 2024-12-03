from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os.path

def chrome_driver(sheets_path):
    # Inicializa o navegador Chrome
    options = webdriver.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_experimental_option("prefs",{
        "download.default_directory": rf'{sheets_path}',
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(options=options)

    # Abrindo um URL no navegador
    driver.get("https://cp10160.varejofacil.com/app/#/login")

    # Aguarda o driver carregar
    sleep(5)

    # ===========================================
    # Campo de login
    login = driver.find_element(By.XPATH, "//input[@data-cy='login-usuario-input-field']")
    login.send_keys('jhonh01')

    sleep(1)

    # Campo de senha
    passw = driver.find_element(By.XPATH, "//input[@data-cy='login-senha-input-field']")
    passw.send_keys('Jhonbruno12@')

    sleep(1)

    # Faz login no sistema
    driver.find_element(By.XPATH, "//button[@data-cy='login-entrar-button']").click()
    # ===========================================

    sleep(5)

    # ===========================================
    # Seleciona o menu Estoque
    driver.find_element(By.XPATH, "//div[@data-cy='sidemenu-item-estoque']").click()

    sleep(2)

    # Seleciona o menu de relatorios
    driver.find_element(By.XPATH, "//div[@data-cy='sidemenu-item-relatorios']").click()

    sleep(2)

    # Seleciona a opção de saldo de estoque
    driver.find_element(By.XPATH, "//a[@data-cy='sidemenu-item-saldo-de-estoque']").click()
    # ===========================================

    sleep(5)

    # ===========================================
    # Seleciona o campo das lojas
    section = driver.find_element(By.CLASS_NAME, "MainGB_mainContent_1z6Zo")

    # Como o conteuno está em um iframe é necessário alterar a interação para ele
    iframe = section.find_element(By.XPATH, "//iframe[@id='legadoFrame']")

    driver.switch_to.frame(iframe)

    itens = driver.find_elements(By.XPATH, "//div[@class='panel panel-default']")

    itens[1].click()

    sleep(1)

    # Clica no campo de adicionar
    driver.find_element(By.XPATH, "//a[@onclick='jQuery.iniciaPopupAdcaoDeLoja()']").click()

    sleep(1)

    # Envia o codigo no campo de codigo loja
    driver.find_element(By.XPATH, "//input[@name='filtro.codigo']").send_keys("23414")

    sleep(2)

    # Clica no botão de pesquisar
    driver.find_element(By.XPATH, "//input[@id='botaoPesquisarPopup']").click()

    sleep(2)

    # Seleciona a loja
    driver.find_element(By.XPATH, "//input[@id='checkPopupPesquisa23414']").click()

    sleep(2)

    # Confirma a seleção
    driver.find_element(By.XPATH, "//button[@id='botaoConcluirSelecaoPopupPesquisa']").click()

    sleep(5)

    # Seleciona a opção Ambos no campo Linha
    ambos = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='ambos']"))
    )
    # Desce a tela até a opção
    driver.execute_script('arguments[0].scrollIntoView(true);', ambos)
    ambos.click()

    # Desmarca a opção de Mostrar Produtos
    mostrar_produtos = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='situacaoEmEstoquePositivo']"))
    )
    # Desce a tela até a opção
    driver.execute_script('arguments[0].scrollIntoView(true);', mostrar_produtos)

    mostrar_produtos.click()

    #seleciona o formato XLS, para isso, aguarda que a opção do radio-button esteja carreagada
    radio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='formatoXLS']"))
    )
    # Desce a tela até a opção
    driver.execute_script('arguments[0].scrollIntoView(true);', radio)

    radio.click()

    sleep(3)

    # Gera o arquivo
    gerar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='gerar']"))
    )
    gerar.click()

    # Verifica se o arquivo já está na pasta para só aí, parar a execução
    while True:
        if os.path.isfile('./sheets/relatorioSaldoEstoque.xls'):
            driver.quit()
            break


