import pyshorteners
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate

#################################################################################################################################################
from .forms import InputURLs, UserCreationForm, UserUpdateForm, ProfileUpdateForm
from .models import URLs, Profile

def profile(request):
    """ Menampilkan konten pada User Profile """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user, prefix='user')
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile, prefix='profile')
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return HttpResponseRedirect('profile-page')
    else:
        u_form = UserUpdateForm(instance=request.user, prefix='user')
        p_form = ProfileUpdateForm(instance=request.user.profile, prefix='profile')

    posts = Profile.objects.filter(user=request.user)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'posts': posts,
    }

    return render(request, 'profile/profile.html', context)

def register(request):
    """ Membuat Form Register """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile-page')
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def home(request):
    """ Membuat Halaman Home """
    if request.method == 'POST':
        inp_form = InputURLs(request.POST)
        if inp_form.is_valid() :
            inp_form.save()
            return HttpResponseRedirect('/')

    else : 
        inp_form = InputURLs(request.POST)

    url = URLs.objects.order_by('-id')
    url_count = URLs.objects.count()
    prof_count = Profile.objects.count()

    context = { 
        'inp_form': inp_form,
        'url': url,
        'count': url_count,
        'prof_count': prof_count,
    }

    return render(request, 'home.html', context)
