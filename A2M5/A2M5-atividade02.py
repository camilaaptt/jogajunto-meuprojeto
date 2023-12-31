from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

#ABRIR NAVEGADOR
navegador = Firefox()

url = "https://www.jogajuntoinstituto.org/"

#ACESSAR SITE
navegador.get(url)

# IDENTIFICAR A BARRA DE PESQUISA
# barra_de_pesquisa = navegador.find_element(By.NAME, "q")
#REALIZAR A PESQUISA
# barra_de_pesquisa.click()
# barra_de_pesquisa.send_keys("Instituto Joga Junto")
# barra_de_pesquisa.send_keys(Keys.ENTER)

form_name = navegador.find_element(By.NAME, "nome")

form_name.send_keys("Camila")

form_email = navegador.find_element(By.NAME, "email").send_keys("camilaaptt@gmail.com")
form_body = navegador.find_element(By.NAME, "body").send_keys("Primeira automação com Selenium WebDriver")
form_select = navegador.find_element(By.NAME, "assunto")


select = Select(form_select)

select.select_by_visible_text("Contratar profissionais")

form_btn = navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button")

print(form_btn)

form_btn.submit()

# resultados.click()