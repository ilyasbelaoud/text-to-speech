from gtts import gTTS
from playsound import playsound

text = input("Enter your text here.")
language = 'en'
speech = gTTS(text=text, lang=language, slow=False)
speech.save("speech.mp3")
playsound("speech.mp3")
