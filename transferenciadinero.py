# Importar las bibliotecas necesarias de Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException  
import time
from selenium import webdriver
import tkinter as tk #popups
from tkinter import messagebox

# Inicializa el navegador (Chrome)
driver = webdriver.Chrome()

# Abre la página web de ParaBank
driver.get("https://parabank.parasoft.com/parabank/index.htm")
driver.maximize_window()

# Espera para asegurar que la página esté cargada
time.sleep(2)

# Inicia sesión
Usernamelog = driver.find_element(By.XPATH, "//input[contains(@name,'username')]").send_keys("karen")
Passwordlog = driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Yaxo8145")
btn_login = driver.find_element(By.XPATH, "//input[@type='submit']")
btn_login.click()

# Espera que la página de la cuenta cargue
time.sleep(2)

# Clic en "Transfer Funds"
Newtransfer = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Transfer Funds')]"))
)
Newtransfer.click()

# Variable cantidad de dinero
Amountenv = "20"
amount = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'amount')]"))
)
amount.send_keys(Amountenv)


fromaccount = "15342"

# Esperar hasta que las opciones en 'fromAccountId' estén cargadas (por el AJAX)
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//select[@id='fromAccountId']/option"))
)

# Verifica y selecciona el ID de la cuenta
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[@id='fromAccountId']"))
)
select_object = Select(select_element)

# Imprimir todas las opciones disponibles (texto y valor, útil para debugging)
print("Opciones en 'fromAccountId':")
for option in select_object.options:
    print(f"Texto visible: '{option.text}' - Valor: '{option.get_attribute('value')}'")

# Intentar seleccionar la opción usando el valor de 'value' o 'text'
try:
   
    select_object.select_by_value(fromaccount) 
except NoSuchElementException:
    print(f"La opción con valor '{fromaccount}' par envío no está disponible.")

toaccount = "15564"

# Esperar hasta que las opciones en 'fromAccountId' estén cargadas (por el AJAX)
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//select[@id='toAccountId']/option"))
)

# Verifica y selecciona el ID de la cuenta
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[@id='toAccountId']"))
)
select_object = Select(select_element)

# Imprimir todas las opciones disponibles (texto y valor, útil para debugging)
print("Opciones en 'toAccountId':")
for option in select_object.options:
    print(f"Texto visible: '{option.text}' - Valor: '{option.get_attribute('value')}'")

# Intentar seleccionar la opción usando el valor de 'value' o 'text'
try:
   
    select_object.select_by_value(toaccount) 
except NoSuchElementException:
    print(f"La opción con valor '{toaccount}' par envío no está disponible.")

# Espera unos segundos para ver el resultado o agregar confirmación
time.sleep(2)

# Clic en el botón para abrir la nueva cuenta
btn_open = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@value='Transfer']"))
)
btn_open.click()

#validar mensaje de registro
try:
    # Busca el elemento con el mensaje de éxito
    msjcreate=driver.find_element(By.XPATH, "//h1[@class='title'][contains(.,'Transfer Complete!')]")
    # Si se encuentra el elemento, muestra el mensaje de éxito
    print("transferencia enviada correctamente")
    messagebox.showinfo("popup", "transferencia enviada correctamente")
except:
    # Si no se encuentra el elemento, muestra un mensaje de error
    print("Parece que hubo un error al enviar")
    messagebox.showerror("Error", "No se pudo enviar")



# Cierra el navegador
driver.quit()