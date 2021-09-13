import re

s = input("Do you agrre?\n")

if re.search("^y(es)?$", s,re.IGNORECASE):
    print("Agreed.")
elif re.search("^n(o)?$", s):
    print("Not agreed.")

"""
Reconociendo por micrófono lo q' se dice... Google

import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("say something!")
    audio = recognizer.listen(source)
print("Google reconocio:")
print(recognizer.recognize_google(audio))
"""

"""
import qrcode

image = qrcode.make("https://link")
image.save("exampel.png", "PNG")
"""