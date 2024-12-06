from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
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
    login.send_keys(os.getenv('user_login_vf'))

    sleep(1)

    # Campo de senha
    passw = driver.find_element(By.XPATH, "//input[@data-cy='login-senha-input-field']")
    passw.send_keys(os.getenv('pass_login_vf'))

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

    loop = True
    # Para a automação quando o arquivo é criado
    while loop:
        for arquivo in os.listdir(sheets_path):
            nome, extesion = os.path.splitext(arquivo)
            if extesion == ".xls":
                driver.quit()
                loop = False

    driver.quit()

def vd_driver(sheets_path, login, passw):
    
    acess_login = login
    pass_login = passw

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

    driver.get("https://sgi.e-boticario.com.br/Paginas/Acesso/Entrar.aspx")

    sleep(5)

    # Insere o login do usuario
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(acess_login) #Usuario
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(pass_login) #Senha

    # Clica no botão de login
    driver.find_element(By.XPATH, "//span[@class='mdc-button__ripple']").click()

    sleep(5)

    # Seleciona o menu Logistica
    driver.find_element(By.XPATH, "//a[@data-target='#submenu-cod-7']").click()

    sleep(1)

    # Seleciona o menu logistica interna
    driver.find_element(By.XPATH, "//a[@href='javascript: void(607);']").click()

    sleep(2)

    # Seleciona o menu Cadastro de Linhas de Separação
    elemento_ul = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//li[@class='has-sub-itens seta-lista submenu-select']/ul"))
    )
    elemento_ul.find_element(By.XPATH, ".//a[text()='Cadastro de Linhas de Separação']").click()

    sleep(2)

    # logistica_menu = driver.find_element(By.XPATH, "//ul[@style='left: -292px; display: block;']")
    # menus = logistica_menu.find_elements(By.TAG_NAME, "li")
    # menus[3].click()

    # sleep(5)

    # Clica no botão de pesquisa da linha de separação
    driver.find_element(By.XPATH, "//a[@id='ContentPlaceHolder1_buscaSeparacao_buscarButton_btn']").click()

    sleep(2)

    # Coloca o mouse encima do texto
    hover = driver.find_element(By.XPATH, "//div[@id='ContentPlaceHolder1_buscaSeparacao_linhasSeparacaoGrid_MenuContextoGrid1_0_gridButton_0']")

    ActionChains(driver).move_to_element(hover).perform()

    # Clica na opção de editar
    driver.find_element(By.XPATH, "//a[@id='ContentPlaceHolder1_buscaSeparacao_linhasSeparacaoGrid_MenuContextoGrid1_0_editarButton_0_btn_0']").click()

    sleep(5)

    # Clica no botão de exportar 
    driver.find_element(By.XPATH, "//a[@id='ContentPlaceHolder1_exportarBotao_btn']").click()

    loop = True
    # Para a automação quando o arquivo é criado
    while loop:
        for arquivo in os.listdir(sheets_path):
            nome, extesion = os.path.splitext(arquivo)
            if extesion == ".xls":
                driver.quit()
                loop = False

    driver.quit()
    

