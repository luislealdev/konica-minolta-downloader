from impresora import impresora
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome()

info = []

driver.get("https://www.konicaminolta.es/es-es/listado-de-productos")

allLinks = driver.find_elements(by=By.CSS_SELECTOR, value="li a")
for link in allLinks:
    href = link.get_attribute('href')
    counter = 0
    if (not "discontinuados" in href and "hardware" in href and counter>1):
        print(href)
        counter+=1
        # driver = webdriver.Chrome()
        # driver.get(href)
        # impresora = impresora()
        # info.append(impresora)

driver.close()
