import os
import speech_recognition as sr
from pytube import YouTube
import openai
openai.api_key = "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"


class ArticleCreator:
    def __init__(self):
        self.completion = openai.Completion()

    def create_article(self, text):
        response = self.completion.create(
          engine="davinci",
          prompt=f"Generate an article from the following text: {text}",
          temperature=0.5,
          max_tokens=1000,
          n = 1,
          stop=None
        )
        return response.choices[0].text


class VideoExtractor:
    def __init__(self, url):
        self.url = url
        self.video = YouTube(self.url)
        self.audio = self.video.streams.filter(only_audio=True).first()

    def extract_data(self):
        audio_file = self.audio.download()
        r = sr.Recognizer()

        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)

        return r.recognize_google(audio_data, language='en-US')
