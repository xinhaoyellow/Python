import speech_recognition as sr
from os import path

def voice2Text(filename):
    vocie_file=path.join(path.dirname(path.realpath(__file__)),filename)
    r=sr.Recognizer()
    with sr.AudioFile(vocie_file) as source:
        audio=r.record(source)
    try:
        content = r.recognize_google(audio, language='zh-CN')
        # print("Google Speech Recognition:" + content)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Google Speech Recognition error; {0}".format(e))
 
    return content 


print(voice2Text('test.wav'))