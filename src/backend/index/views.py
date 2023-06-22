from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .razer import razer

# Create your views here.


@csrf_exempt
def Index(request):
    if request.method == 'POST': 
        url = request.POST.get('url')
        print(url)

    # context = razer(url)

    return render(request, 'index.html')
