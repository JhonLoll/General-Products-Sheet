# Importações
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Variáveis de informação de login
nome_usuario = 'jhonh01'
senha_usuario = 'Jhonbruno12@'

# Abre o navegador Chrome
driver = webdriver.Chrome()
# Abre o site
driver.get('https://cp10160.varejofacil.com/app/#/login')
sleep(5)

# Localiza e insere as informações no campo de Usuario
campo_nome_usuario = driver.find_element(By.XPATH, "//*[@id='input-132']")
campo_nome_usuario.click()
campo_nome_usuario.send_keys(nome_usuario)

# Localiza e insere as informações do campo de Senha
campo_senha_usuario = driver.find_element(By.XPATH, "//*[@id='password']")
campo_senha_usuario.click
campo_senha_usuario.send_keys(senha_usuario)

# Localiza e pressiona o botão de login
driver.find_element(By.XPATH, "//input[@data-cy='login-entrar-sso-button']").click