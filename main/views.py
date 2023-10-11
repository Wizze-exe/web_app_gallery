from django.shortcuts import render
from .models import Arts

# Create your views here.
def index(request):
    arts = Arts.objects.all()
    return render(request, 'main/index.html', {'arts': arts})

def art(request):
    return render(request, 'main/art.html')