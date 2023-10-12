from django.shortcuts import render, redirect
from .models import Arts
from .forms import ArtForm


# Create your views here.
def index(request):
    arts = Arts.objects.all()
    return render(request, 'main/index.html', {'arts': arts})


def art(request):
    error = ''
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'форма неверна'
    form = ArtForm()
    data = {
        'artForm': form,
        'error': error
    }
    return render(request, 'main/art.html', data)
