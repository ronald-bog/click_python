from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configura el WebDriver (aquí se usa Chrome como ejemplo)
driver_path = "ruta/al/chromedriver"  # Reemplaza con la ruta a tu ChromeDriver
driver = webdriver.Chrome(driver_path)

# Abre la URL de la aplicación
driver.get("https://ejemplo.com")  # Reemplaza con la URL de tu página

# Espera a que el botón esté disponible
time.sleep(3)  # Usa WebDriverWait para una espera más precisa en proyectos avanzados
 
# Encuentra el botón por su ID, clase, nombre, o XPath
boton = driver.find_element(By.ID, "id_del_boton")  # Cambia ID por el identificador correcto

# Haz clic en el botón
boton.click()
print("Clic realizado en el botón")

# Espera 9 segundos y vuelve a hacer clic (repetición)
while True:
    time.sleep(9)
    boton.click()
    print("Clic realizado nuevamente en el botón")

###
from pywinauto import Application
import time

# Conéctate a la ventana de la aplicación deseada
app = Application(backend="uia").connect(
    # Cambia "Nombre de la Ventana"
    title="Precios, gráficos y capitalizaciones de mercado de criptomonedas | CoinMarketCap")

# Selecciona la ventana
window = app.window(
    title="Precios, gráficos y capitalizaciones de mercado de criptomonedas | CoinMarketCap")

# Identifica el botón por su identificador (ID, texto, etc.)
# Cambia "Texto del Botón"
boton = window.child_window(title="Abrir", control_type="Button")

# Haz clic en el botón cada 9 segundos
while True:
    boton.click()
    print("Clic realizado en el botón")
    time.sleep(3)
