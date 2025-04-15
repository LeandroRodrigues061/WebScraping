from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

driver = webdriver.Edge()
driver.get("https://www.caixa.gov.br/voce/habitacao/imoveis-venda/Paginas/default.aspx")

btn = driver.find_element(By.CLASS_NAME, "btn.orange.btn-big")
btn.click()

sleep(1)

select01 = driver.find_element(By.CLASS_NAME, "select-button")
select01.click()

select01 = driver.find_element(By.ID, "cmb_estado")
dropdown = Select(select01)
dropdown.select_by_value("SP")
sleep(1)

select02 = driver.find_element(By.CLASS_NAME, "select-button")
select02.click()
select02 = driver.find_element(By.ID, "cmb_cidade")
dropdown2 = Select(select02)
dropdown2.select_by_value("9859")
sleep(1)

driver.quit()