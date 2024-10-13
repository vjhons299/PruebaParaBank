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

# Clic en "Open New Account"
Newaccount = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Open New Account')]"))
)
Newaccount.click()

# Seleccionar el tipo de cuenta (SAVINGS)
select_type = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[contains(@id,'type')]"))
)
select_object_type = Select(select_type)
select_object_type.select_by_visible_text("SAVINGS")

# Definir una variable para el ID de la cuenta
cuenta_id = "15342"

# Verifica y selecciona el ID de la cuenta
select_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//select[contains(@id,'fromAccountId')]"))
)
select_object = Select(select_element)

# Imprimir todas las opciones disponibles (útil para debugging)
for option in select_object.options:
    print("Valor disponible: ", option.text)

# Intentar seleccionar la opción usando la variable 'cuenta_id'
try:
    select_object.select_by_visible_text(cuenta_id)
except NoSuchElementException:
    print(f"La opción '{cuenta_id}' no está disponible.")

# Clic en el botón para abrir la nueva cuenta
btn_open = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".button:nth-child(1)"))
)
btn_open.click()

#validar mensaje de registro
try:
    # Busca el elemento con el mensaje de éxito
    msjcreate=driver.find_element(By.XPATH, "//p[contains(.,'Congratulations, your account is now open.')]")
    # Si se encuentra el elemento, muestra el mensaje de éxito
    print("cuenta creada correctamente")
    messagebox.showinfo("popup", "cuenta creada correctamente")
except:
    # Si no se encuentra el elemento, muestra un mensaje de error
    print("Parece que hubo un error al crear la ceunta.")
    messagebox.showerror("Error", "No se pudo crear la cuenta.")


# Espera unos segundos para ver el resultado
time.sleep(2)

# Cierra el navegador
driver.quit()