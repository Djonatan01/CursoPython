import pyautogui
import time

# Apertando a tecla windows
pyautogui.press("Win")

# Aguarde um momento para o menu aparecer completamente (ajuste conforme necessário)
time.sleep(1)

# Digite "chrome" e pressione Enter
pyautogui.write("chrome")
pyautogui.press("Enter")
