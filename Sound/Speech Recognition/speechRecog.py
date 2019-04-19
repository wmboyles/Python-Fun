import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
from TTS_output import textToSpeech

sd.default.samplerate = 44100
sd.default.channels = 2

# Record speech from the microphone to a given file for a given duration. Optional playback.
def recordToFile(duration=5, filename="output.wav", playback=False, onEnter=False):
    #wait for key press if applicable
    if onEnter: input("Press ENTER to record")
    
    #Record the audio
    print("Recording")
    myrecording = sd.rec(int(duration * sd.default.samplerate))
    sd.wait()

    #Play the audio if requested
    if playback:
        print("Playing")
        sd.play(myrecording)
        sd.wait()

    #Save the audio to a .wav file
    print("Saving")
    sf.write(filename, myrecording, sd.default.samplerate)


# Try to get a transcript of an audio file
def speechRecognize(filename="output.wav"):
    r = sr.Recognizer()
    audio = sr.AudioFile(filename)

    with audio as source:
        audioData = r.record(source)

    try:
        text = r.recognize_google(audioData) #This version uses Google speech recognition, but go unsupported at any time
        #text = r.recognize_sphinx(audioData) #This version is offline, but not very accurate
        return text
    except sr.UnknownValueError:
        print("ERROR -- No Speech found")


while True:
    recordToFile(onEnter=True)
    text = speechRecognize()
    print(text)
