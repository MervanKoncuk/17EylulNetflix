from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.
def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        resim = request.FILES['resim']
        telefon = request.POST['telefon']
        sifre1 = request.POST['sifre1']
        sifre2 = request.POST['sifre2']
        
        if kullanici != '' and email != '' and sifre1 != '' and sifre2 != '':
            if sifre1 == sifre2:
                if User.objects.filter(username = kullanici).exists():
                    messages.error(request, 'Bu kullanıcı adı zaten mevcut')
                    return redirect('register')
                elif User.objects.filter(email = email).exists():
                    messages.error(request, 'Bu email kullanımda')
                    return redirect('register')
                elif len(sifre1) < 6:
                    messages.error(request, 'Şifre en az 6 karakter olmalıdır')
                    return redirect('register')
                elif kullanici.lower() in sifre1.lower():
                    messages.error(request, 'Kullanıcı adı ve şifre benzer olmamalıdır')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username = kullanici, email = email, password = sifre1)
                    Hesap.objects.create(
                        user = user,
                        resim = resim,
                        tel = telefon
                    )
                    user.save()
                    messages.success(request, 'Kullanıcı oluşturuldu')
                    return redirect('index')
            else:
                messages.error(request, 'Şifreler uyuşmuyor')        
                return redirect('register')
        else:
            messages.error(request, 'Tüm alanların doldurulması zorunludur')        
            return redirect('register')
    return render(request, 'register.html')


def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']
        
        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş yapıldı')
            return redirect('profiles')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre hatalı')
            return redirect('login')

    return render(request, 'login.html')

def profiles(request):
    profiller = Profile.objects.filter(user = request.user)
    context = {
        'profiller':profiller
    }
    return render(request, 'browse.html', context)

def olustur(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            if Profile.objects.filter(user = request.user).count() < 4:
                user = form.save(commit=False)
                user.user = request.user
                user.save()
                messages.success(request, 'Profil oluşturuldu')
                return redirect('profiles')
            else:
                messages.error(request, 'En fazla 4 profil oluşturulabilir')
                return redirect('profiles')
    context = {
        'form':form
    }
    return render(request, 'olustur.html', context)

def hesap(request):
    return render(request, 'hesap.html')

def userDelete(request):
    user = request.user
    user.delete()
    messages.success(request, 'Kullanıcı silindi')
    return redirect('index')

def userLogout(request):
    logout(request)
    messages.success(request, 'Çıkış yapıldı')
    return redirect('index')