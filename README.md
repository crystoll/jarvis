# My Virtual Assistant

## Prerequisites

- Python installed and set up (virtual env preferred)
- pip installed, libraries installed
    pip install -r requirements.txt

Alternatively, you can just do something like:

```bash
pip install TTS SpeechRecognition pyaudio openai python-dotenv sounddevice preferredsoundplayer autopep8
```

To use the GPT you need an OpenAI API key, and need an .env file with the key in it.  The .env file should be in the same directory as the main.py file.  The .env file should have the following line in it:

OPENAI_API_KEY=yourkeyhere

Alternatively, you can set the environment variable OPENAI_API_KEY to your key and remove the .env file reading parts.

Alternatively, you can replace OpenAI API with a cool local model instead (Future development idea)

You may need to tinker with the device numbers depending on your machine's setup, which port each device is on, etc.  If code doesn't work for you you can try to use Python libraries to list device ids and names so you can find your proper microphone and speaker device numbers. Alternatively, can of course go wild about the code and make it detect suitable ones and skip bad ones instead of hardcoding them.

## Use

This is just a brief proof-of-concept style of thing, so nothing you could not cook up in a few minutes yourself.  It is just a simple command line interface.  Run the jarvis.py file and it will wait for your audio input, then it will send whatever you say to OpenAI, and then it will read the response out loud to you.  Then it will wait for your next input.

it will prompt you for input.  Type in a question and it will give you an answer.  Type in "quit" to quit.
