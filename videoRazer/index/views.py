from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Video
from .extractor import VideoExtractor, ArticleCreator
from .token_creator import TokenCreator

secret_key = "Y0urS3cr3tK3yH3r3"

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            video = Video(
                  title=data.get('title'),
                  url=data.get('url'),
                  category=data.get('category'),
                  author=data.get('author')
            )
            video.save()

            extractor = VideoExtractor(video.url)
            text = extractor.extract_data()

            creator = ArticleCreator()
            article = creator.create_article(text)

            payload = {"user_id": video.id, "role": "user"}
            token_creator = TokenCreator(secret_key)
            token = token_creator.create_token(payload)

            return JsonResponse({"status": "success", "article": article, "token": token})

        except Exception as e:
            return JsonResponse({"status": "fail", "message": str(e)})
        


def index(request):
    obj = register(request)
    return render(request, './index.html')
