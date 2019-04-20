import speech_recognition as sr


# Try to get a transcript of an audio file
def speechRecognize(filename="output.wav"):
    r = sr.Recognizer()
    audio = sr.AudioFile(filename)

    with audio as source:
        audioData = r.record(source)

    try:
        text = r.recognize_google(audioData)  # This version uses Google speech recognition, but go unsupported at any time
        # text = r.recognize_sphinx(audioData) #This version is offline, but not very accurate
        return text
    except sr.UnknownValueError:
        print("ERROR -- No Speech found")
