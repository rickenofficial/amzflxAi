import pyautogui
import pytesseract
from PIL import ImageGrab
import time

# Configura la ruta de Tesseract si es necesario
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Número máximo de intentos para hacer scroll y encontrar precios
MAX_INTENTOS = 5

def detectar_precios(intentos=0):
    # Captura la pantalla de una región específica donde aparecen los bloques
    screenshot = ImageGrab.grab(bbox=(10, 10, 500, 500))  # Ajusta las coordenadas según tu pantalla
    screenshot.save("captura.png")  # Guarda la imagen para verificar si todo está bien
    text = pytesseract.image_to_string(screenshot)

    precios = extraer_precios(text)

    if not precios:  # Si no hay bloques disponibles, realiza scroll
        if intentos < MAX_INTENTOS:
            hacer_scroll(intentos + 1)
        else:
            print("No se encontraron precios después de múltiples intentos.")
        return False

    # Revisa los precios
    for precio in precios:
        if precio > 110:
            hacer_click_en_bloque(precio)
            return True
    return False

def extraer_precios(text):
    # Lógica para extraer precios del texto
    precios = []
    for linea in text.splitlines():
        try:
            valor = float(linea.replace('$', '').strip())
            precios.append(valor)
        except ValueError:
            pass
    return precios

def hacer_scroll(intentos):
    pyautogui.scroll(-300)  # Desplazamiento hacia abajo
    time.sleep(1)  # Espera para que los nuevos bloques carguen
    detectar_precios(intentos)  # Intenta de nuevo detectar precios

def hacer_click_en_bloque(precio):
    # Lógica para hacer clic en el bloque que cumple la condición
    print(f"Bloque con precio ${precio} encontrado y seleccionado.")
    # Aquí puedes añadir código para hacer clic en las coordenadas del bloque

# Ejecutar la detección de precios
detectar_precios()
