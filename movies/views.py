from django.shortcuts import render, redirect
from .models import *
from user.models import *
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def movies(request, slug, id):
    profil = Profile.objects.filter(slug = slug).get(id = id)
    filmler = Movie.objects.all()
    populer = Movie.objects.filter(kategori__isim = "Popüler")
    gundem = Movie.objects.filter(kategori__isim = "Gündemde")
    profiller = Profile.objects.filter(user = request.user)
    context = {
        'filmler':filmler,
        'populer':populer,
        'gundem':gundem,
        'profil':profil,
        'profiller':profiller
    }
    return render(request, 'browse-index.html', context)

def search(request):
    filmler = ''
    search = ''
    if request.GET.get('search'):
        search = request.GET.get('search')
        filmler = Movie.objects.filter(
            Q(isim__icontains = search) |
            Q(kategori__isim__icontains = search)
        )
    context = {
        'filmler':filmler,
        'search':search
    }
    return render(request, 'search.html', context)

def video(request, filmId):
    film = Movie.objects.get(id = filmId)
    context = {
        'film':film
    }
    return render(request, 'video.html', context)

def view_404(request, exception):
    return redirect('/')