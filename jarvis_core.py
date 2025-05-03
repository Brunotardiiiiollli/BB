import speech_recognition as sr
import pyttsx3
import os
import webbrowser
from playsound import playsound

voz_engine = pyttsx3.init()
voz_engine.setProperty('rate', 175)
voz_engine.setProperty('volume', 1.0)
voz_engine.setProperty('voice', voz_engine.getProperty('voices')[1].id)

def falar(texto):
    playsound("audio/efeito_comando.mp3")
    voz_engine.say(texto)
    voz_engine.runAndWait()

def iniciar_jarvis():
    playsound("audio/efeito_ia.mp3")
    falar("Sim senhor. Assistente iniciado.")

    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as mic:
            print("Aguardando comando...")
            audio = recognizer.listen(mic)

        try:
            comando = recognizer.recognize_google(audio, language="pt-BR").lower()
            print(f"Você disse: {comando}")

            if "sexta-feira" in comando:
                if "abrir navegador" in comando:
                    webbrowser.open("https://www.google.com")
                    falar("Abrindo navegador, senhor.")
                elif "youtube" in comando:
                    webbrowser.open("https://www.youtube.com")
                    falar("Abrindo YouTube, senhor.")
                elif "whatsapp" in comando:
                    webbrowser.open("https://web.whatsapp.com")
                    falar("Abrindo WhatsApp Web, senhor.")
                elif "tocar música" in comando:
                    os.system("start wmplayer")
                    falar("Tocando música, senhor.")
                elif "desligar" in comando:
                    falar("Ok senhor. Fico à disposição.")
                    break
                else:
                    falar("Sim senhor. Já respondo.")
                    # Aqui pode entrar resposta da API da OpenAI

        except Exception as e:
            print("Erro:", e)
