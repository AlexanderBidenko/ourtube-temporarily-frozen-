from googletrans import Translator
from string_processing import lineal_string as ls
file = "file.txt"
text = ls(file)


translator = Translator()

w = translator.translate(text)

print(w.text)
