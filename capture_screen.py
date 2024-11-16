import pyautogui
from PIL import ImageGrab

# Capturar una parte de la pantalla (ajusta las coordenadas según tu necesidad)
def capturar_pantalla():
    # Ajusta las coordenadas según la región de la pantalla que deseas capturar
    bbox = (10, 10, 500, 500)
    captura = ImageGrab.grab(bbox)
    captura.save("captura.png")
    print("Captura de pantalla guardada como captura.png")

# Ejecutar la función de captura de pantalla
capturar_pantalla()
