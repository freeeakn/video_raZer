from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import UrlForm
from .razer import razer

# Create your views here.

@csrf_exempt
def Index(request):
    if request.method == "POST":
        url = request.POST.get('url')
        print(url)
        data = razer(url)
        print(data)
        return HttpResponse(f"<h2>{ data[0]['start'] }</h2><br><p>{ data[0]['text'] }</p>")
    else:
        form = UrlForm()
        return render(request, "index.html", {"form": form})



