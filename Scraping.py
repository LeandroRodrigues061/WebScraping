from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Edge()
driver.get("https://vitrinebradesco.com.br/auctions?type=realstate")

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "select__control")))

dropdowns = driver.find_elements(By.CLASS_NAME, "select__control")
dropdowns[0].click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'SP')]"))).click()

dropdowns = driver.find_elements(By.CLASS_NAME, "select__control")  
dropdowns[1].click()
wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(), 'São Paulo - SP')])[2]"))).click()

sleep(2)

# #Como a página carrega os imóveis de forma assíncrona e não tem paginação, foi preciso fazer um scroll automático para baixo até que não haja mais imóveis a serem carregados.
# last_height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     sleep(2)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

#     sleep(3)

def extrair_dados():
    cards = driver.find_elements(By.CLASS_NAME, "auction-container")
    dados = []

    for card in cards:
        try:
            ActionChains(driver).move_to_element(card).perform()
            sleep(0.5)
            imagem_element = card.find_element(By.CLASS_NAME, "thumbnail-container").find_element(By.TAG_NAME, "img")
            imagem = imagem_element.get_attribute("src")
        except:
            imagem = "N/A"

        try:
            descricao = card.find_element(By.CLASS_NAME, "description").text
        except:
            descricao = "N/A"

        try:
            valor = card.find_element(By.CLASS_NAME, "bottom").text.split("\n")[0]
        except:
            valor = "N/A"

        dados.append({
            "imagem": imagem,
            "descricao": descricao,
            "valor": valor
        })

    return dados


with open("imoveis_bradesco.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    writer = csv.DictWriter(arquivo_csv, fieldnames=["imagem", "descricao", "valor"])
    writer.writeheader()
    for dado in extrair_dados():
        writer.writerow(dado)

driver.quit()
