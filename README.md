# Proyecto de Automatización Bonbonite
Este proyecto automatiza casos de prueba de Login y Compra para el sitio web de Bonbonite utilizando **Python**, **Selenium**, **pytest** y **webdriver-manager**.

## Herramientas
- Lenguaje: Python 3.13.5
- Framework: Selenium
- Librerías: pytest, dotenv

## Instrucciones
1. Instalar dependencias:
   pip install -r requirements.txt

2. Ejecutar las pruebas:
   pytest casos_de_prueba/login_test.py
   pytest casos_de_prueba/compra_test.py

## Estructura del proyecto
bonbonite-automation/
> casos_de_prueba/ # Carpeta que contiene los scripts de pruebas automatizadas
- compra_test.py # Script de prueba para el proceso de compra
- login_test.py # Script de prueba para el inicio de sesión

> venv/ # Entorno virtual de Python
- Include/ # Archivos de inclusión del entorno virtual
- Lib/ # Librerías instaladas en el entorno virtual
- Scripts/ # Scripts ejecutables del entorno virtual

> .env # Archivo de variables de entorno

> README.md # Documentación del proyecto

> requirements.txt # Lista de dependencias del proyecto

## Roles
Responsable QA: Alejandra María Alvis Salgado
Cliente: Bon-bonite
Revisor: Gerente de Mercadeo y Ventas
