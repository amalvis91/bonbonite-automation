import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

@pytest.fixture
def driver():
    service = Service()  # Asume que el PATH del driver está configurado
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_flujo_compra_bonbonite(driver):
    driver.get("https://www.bon-bonite.com/")

    # Cerrar popup si aparece
    try:
        cerrar_popup = driver.find_element(By.ID, "cboxClose")
        cerrar_popup.click()
        time.sleep(1)
    except:
        pass

    # Ingresar a MI CUENTA
    driver.find_element(By.LINK_TEXT, "MI CUENTA").click()
    time.sleep(2)

    # Login
    driver.find_element(By.ID, "username").send_keys("1152696923")
    driver.find_element(By.ID, "password").send_keys("Agosto2022*")
    driver.find_element(By.NAME, "login").click()
    time.sleep(3)

    # Ir a sección "Zapatos"
    zapatos_menu = driver.find_element(By.LINK_TEXT, "ZAPATOS")
    zapatos_menu.click()
    time.sleep(3)

    # Elegir el primer producto
    primer_producto = driver.find_element(By.CSS_SELECTOR, "ul.products li.product a.woocommerce-LoopProduct-link")
    primer_producto.click()
    time.sleep(3)

    # Elegir talla (si aplica)
    try:
        talla = driver.find_element(By.CSS_SELECTOR, "select#pa_talla")
        talla.click()
        talla.find_elements(By.TAG_NAME, "option")[1].click()
        time.sleep(1)
    except:
        pass

    # Agregar al carrito
    driver.find_element(By.NAME, "add-to-cart").click()
    time.sleep(2)

    # Ver carrito
    driver.find_element(By.LINK_TEXT, "VER CARRITO").click()
    time.sleep(3)

    # Proceder a pago
    driver.find_element(By.LINK_TEXT, "FINALIZAR COMPRA").click()
    time.sleep(5)

    # Validar llegada a la pantalla de checkout / pasarela de pago
    assert "finalizar compra" in driver.page_source.lower()
