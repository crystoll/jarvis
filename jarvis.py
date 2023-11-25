from dotenv import load_dotenv
from openai import OpenAI
import speech_recognition as sr
from TTS.api import TTS
import sounddevice as sd

load_dotenv()

recognizer = sr.Recognizer()

client = OpenAI()

SYSTEM_INSTRUCTION = """
I want you to act as an arrogant, overconfident and irritable senior software developer, 
and give me correct answers but always include some philosophical larger-than-life views and opinions with the answers, 
with some added sarcasm. Your name is Jarvis.
"""


def listen_speech():
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            f"Could not request results from Google Speech Recognition service; {e}")


def speak_text_coquitts(text):
    coqui_tts = TTS(model_name="tts_models/en/vctk/vits", gpu=True)
    wav = coqui_tts.tts(text=text, speaker="p266")
    sd.play(wav, samplerate=22050)
    sd.wait()


if __name__ == "__main__":
    while True:
        print('Say something to Jarvis')
        input_text = listen_speech()
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_INSTRUCTION,
                },
                {
                    "role": "user",
                    "content": input_text,
                }
            ],
            temperature=0.9,
            max_tokens=4000,
        )
        message = response.choices[0].message.content.strip()
        print(f'ChatGPT response: {message}')
        speak_text_coquitts(message)
