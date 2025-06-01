import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import time
import math
import operator
import pywhatkit 
import webbrowser

# --- Sesli yanıt verme ---
def speak(text):
    tts = gTTS(text=text, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

# --- Ses kaydı alma ---
def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Dinliyor...")
        audio = r.listen(source)
        try:
            voice = r.recognize_google(audio, language="tr-TR")
            print("🗣️ Sen söyledin:", voice)
            return voice.lower()
        except sr.UnknownValueError:
            speak("Seni anlayamadım.")
        except sr.RequestError:
            speak("Sistem çalışmıyor.")
    return ""

# --- Web arama taklidi ---
def web_search(query):
    if "einstein" in query:
        return "Einstein, görelilik teorisiyle tanınan bir fizikçidir."
    elif "atatürk" in query:
        return "Mustafa Kemal Atatürk, Türkiye Cumhuriyeti'nin kurucusudur."
    else:
        return "İnternette bu konuda bir bilgi bulamadım."

# --- Matematik işlemleri ---
def hesapla(komut):
    komut = komut.replace("çarpı", "*").replace("artı", "+").replace("eksi", "-").replace("bölü", "/")
    try:
        sonuc = eval(komut)
        return f"Sonuç: {sonuc}"
    except:
        return "Bu matematik işlemini anlayamadım."

# --- TXT kaydetme ---
def kaydet_txt():
    speak("Ne yazmamı istersin?")
    icerik = record()
    if icerik:
        with open("not.txt", "a", encoding="utf-8") as dosya:
            dosya.write(icerik + "\n")
        speak("Not kaydedildi.")
    else:
        speak("Herhangi bir şey algılanmadı.")

# --- Başlangıç mesajı ---
speak("Asistan başlatıldı. hey asistan diyerek başlatabilirsiniz")

# --- Döngü ---
while True:
    komut = record()




    # Hey Asistan → komutlara geç
    if "hey asistan" in komut:

        # Alt komutları dinle
        speak("Mod seçin: matematik, hava, eğlence, arama, not veya çıkış.")
        alt_komut = record()

        # 4️⃣ Matematik
        if "matematik" in alt_komut:
            speak("İşlemi söyleyin.")
            islem = record()
            sonuc = hesapla(islem)
            speak(sonuc)

        # 6️⃣ Arama
        elif "arama" in alt_komut:
            speak("Ne aramak istersin?")
            sorgu = record()
            cevap = web_search(sorgu)
            speak(cevap)

        # 7️⃣ Hava durumu
        elif "hava" in alt_komut:
            speak("Bugün Samsun'da hava parçalı bulutlu ve 22 derece.")

        # Eğlence
        elif "eğlence" in alt_komut or "şaka" in alt_komut:
            speak("Neden bilgisayar kahve içemez? Çünkü Java'sı yok!")

        # Not alma
        elif "not" in alt_komut or "kaydet" in alt_komut:
            kaydet_txt()

        # Çıkış
        elif "çık" in alt_komut or "kapat" in alt_komut:
            speak("asistan kapatılıyor")
            break

        else:
            speak("Bu modu anlayamadım.")

    # Genel çıkış
    elif "kapat" in komut or "çık" in komut:
        speak("Görüşmek üzere.")
        break

    # Tanınmayan komut
    elif komut != "":
        speak("Bu komutu bilmiyorum.")
