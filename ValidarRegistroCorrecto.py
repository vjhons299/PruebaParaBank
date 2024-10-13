# Importa la clase webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import tkinter as tk #popups
from tkinter import messagebox



#variable tiempo para mantener la pestaña abierta
tiempo=5
# Inicializa un objeto Chrome (navegador) 
driver=webdriver.Chrome()
# Abre la página web en el navegador
driver.get("https://parabank.parasoft.com/parabank/index.htm")
# Agrandar pantalla
driver.maximize_window()
time.sleep(2)
# Dar clic en botón registrar
register=driver.find_element(By.XPATH, "//a[contains(.,'Register')]")
register.click()
time.sleep(2)
# Ubicar campos a ingresar
Firstname=driver.find_element(By.XPATH, "//input[@id='customer.firstName']").send_keys("John sebastián")
Lastname=driver.find_element(By.XPATH, "//input[@id='customer.lastName']").send_keys("vargas lasso")
Adress=driver.find_element(By.XPATH, "//input[@id='customer.address.street']").send_keys("Calle 41b sur")
City=driver.find_element(By.XPATH, "//input[@id='customer.address.city']").send_keys("bogotá")  
State=driver.find_element(By.XPATH, "//input[@id='customer.address.state']").send_keys("bogotá") 
zipcode=driver.find_element(By.XPATH, "//input[@id='customer.address.zipCode']").send_keys("112343") 
Phonenumb=driver.find_element(By.XPATH, "//input[@id='customer.phoneNumber']").send_keys("3007562171") 
Ssn=driver.find_element(By.XPATH, "//input[@id='customer.ssn']").send_keys("Yaxo8145") 

user=driver.find_element(By.XPATH, "//input[@id='customer.username']").send_keys("karen")
passw=driver.find_element(By.XPATH, "//input[@id='customer.password']").send_keys("Yaxo8145")
rpassw=driver.find_element(By.XPATH, "//input[@id='repeatedPassword']").send_keys("Yaxo8145")

btn_register=driver.find_element(By.XPATH, "//input[@value='Register']")
btn_register.click()

#validar mensaje de registro
try:
    # Busca el elemento con el mensaje de éxito
    msj=driver.find_element(By.XPATH, "//p[contains(.,'Your account was created successfully. You are now logged in.')]")
    # Si se encuentra el elemento, muestra el mensaje de éxito
    print("registrado correctamente")
    messagebox.showinfo("popup", "Registrado Correctamente")
except:
    # Si no se encuentra el elemento, muestra un mensaje de error
    print("Parece que hubo un error al registrarte.")
    messagebox.showerror("Error", "No se pudo registrar la cuenta.")


time.sleep(tiempo)
driver.quit()

   


