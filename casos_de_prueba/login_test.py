import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

@pytest.fixture
def driver():
    service = Service()  # Asume que el PATH del driver está configurado
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_login_bonbonite(driver):
    driver.get("https://www.bon-bonite.com/")

    # Cerrar popup si aparece
    try:
        cerrar_popup = driver.find_element(By.ID, "cboxClose")
        cerrar_popup.click()
        time.sleep(1)
    except:
        pass

    # Ir a "Mi cuenta"
    mi_cuenta = driver.find_element(By.LINK_TEXT, "MI CUENTA")
    mi_cuenta.click()
    time.sleep(2)

    # Ingresar usuario y contraseña ya registrado previamente para efectos de la prueba
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    username_input.send_keys("1152696923")
    password_input.send_keys("Agosto2022*")

    # Clic en el botón de login
    login_button = driver.find_element(By.NAME, "login")
    login_button.click()
    time.sleep(3)

    # Verificar si se mostró el nombre del usuario (u otro indicador de sesión iniciada)
    assert "mi cuenta" in driver.page_source.lower()