from django.shortcuts import render, redirect
from .models import Show
# Create your views here.
def index(request):
    context = {
        'shows': Show.objects.all
    }
    return render(request, 'show.html', context)

def new(request):
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return render(request, 'index.html')
