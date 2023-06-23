from youtube_transcript_api import YouTubeTranscriptApi
import re

# nltk.download('stopwords')

def get_video_id(link):
    pattern = r"(?:https?:\/\/(?:www\.)?youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(pattern, link)
    if match:
        video_id = match.group(1)
    return video_id

def razer(url):
    video_url = str(url)
    video_id = get_video_id(video_url)
    video_text = ""

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    except:
        print("Programm can process only video with subtitles")
        exit(1)

    for transcript in transcript_list:
        # for phrase in transcript.translate('en').fetch() : # ПЕРЕВОД (русский это ru)
        for phrase in transcript.fetch() :
            video_text += phrase['text'] + " "
        return transcript.translate('ru').fetch()
        break