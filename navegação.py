from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome(executable_path="./chromedriver.exe")

# Abrir o navegador no site: https://www.mercadolivre.com.br/
driver.get("https://www.mercadolivre.com.br/")

driver.implicitly_wait(2)
sleep(2)

driver.maximize_window()

# Clicar no botão Entendi
botão = driver.find_element_by_id('newCookieDisclaimerButton')

try:
    botão.click()
except:
    print("\033[1;31mNão foi possívelclicar no botão\033[m")

# Realizar primeira busca
busca1 = driver.find_element_by_name('as_word')

busca1.send_keys('mouse sem fio recarregável multilaser mo277')
sleep(1)
busca1.send_keys(Keys.ENTER)

sleep(2)

# Entrar no primeiro produto
link1 = driver.find_element_by_xpath(
    '//*[@id="root-app"]/div/div[1]/section/ol[1]/li[1]/div/div/a').get_attribute("href")

try:
    driver.get(link1)
except:
    print("\033[1;31mNão foi possível acessar o produto.\033[m")

sleep(1)

# - Nome
nome1 = driver.find_element_by_class_name('ui-pdp-title').text

# - Preço
simbolo1 = driver.find_element_by_class_name('price-tag-symbol').text
inteiro1 = driver.find_element_by_class_name('price-tag-fraction').text
decimal1 = driver.find_element_by_class_name('price-tag-cents').text

# - Avaliação
avaliação1 = driver.find_element_by_class_name('ui-pdp-reviews__rating__summary__average').text

driver.refresh()
sleep(1)

# Realizar segunda busca
busca2 = driver.find_element_by_class_name('nav-search-input')
busca2.send_keys('teclado redragon kumara preto e vermelho')
sleep(1)
busca2.send_keys(Keys.ENTER)

driver.implicitly_wait(2)

# Entrar no segundo produto
link2 = driver.find_element_by_xpath(
    '//*[@id="root-app"]/div/div[1]/section/ol[1]/li[1]/div/div/a').get_attribute("href")

driver.get(link2)

sleep(1)

# - Nome
nome2 = driver.find_element_by_class_name('ui-pdp-title').text

# - Preço
simbolo2 = driver.find_element_by_class_name('price-tag-symbol').text
inteiro2 = driver.find_element_by_class_name('price-tag-fraction').text
decimal2 = driver.find_element_by_class_name('price-tag-cents').text

# - Avalição
avaliação2 = driver.find_element_by_xpath(
    '//*[@id="root-app"]/div[2]/div[2]/div[3]/div[1]/div[2]/div/section/header/div/div[1]/p').text

# Fechar o navegador
driver.close()

# Exibir os resultados buscados
resultados = f'''\033[1;32m
Primeiro Produto:
- Nome: {nome1}
- Preço: {simbolo1}{inteiro1},{decimal1}
- Avaliação: {avaliação1}

Segundpo Produto:
- Nome: {nome2}
- Preço: {simbolo2}{inteiro2},{decimal2}
- Avaliação: {avaliação2}
\033[m'''

print(resultados)

print("\033[1;32m\nProcesso finalizado com sucesso.\033[m")