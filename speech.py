import speech_recognition

def speech(lang="pl-PL"):
    mic = speech_recognition.Microphone()
    recog = speech_recognition.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        print("Nagrywanie rozpoczęte")
        audio = recog.listen(audio_file)
        print("Nagrywanie zakończone")

        return recog.recognize_google(audio, language=lang)
