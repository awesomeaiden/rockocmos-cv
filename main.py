import cv2
from googletrans import Translator

# Sample translation
translator = Translator()
translation = translator.translate("Образец русских слов")
print(translation.text)