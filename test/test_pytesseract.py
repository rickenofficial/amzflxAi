from PIL import Image
import pytesseract

# Configura la ruta de Tesseract si es necesario
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Carga la imagen para probar
image = Image.open('ruta/a/tu/imagen.png')  # Asegúrate de que esta ruta sea correcta
texto = pytesseract.image_to_string(image)

# Imprime el texto extraído
print(texto)
