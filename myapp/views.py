from django.urls import reverse
from django.core import serializers
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForm, UserUpdateForm, ProfileUpdateForm, CustomForm, UpdateCustomForm
from .models import CustomURLs

def payment(request):
    return render(request, 'profile/payment.html')

def brand(request):
    a = CustomURLs.objects.all()
    return render(request, 'profile/brand.html', {'a': a})

@login_required
def url(request): 
    form    = CustomForm()
    cus     = CustomURLs.objects.filter(user=request.user).order_by('-id')

    context = {'custom': cus, 'form': form }
    return render(request, 'profile/urls.html', context)

def create(request):
    data = {}
    if request.POST.get('action') == 'post':
        long_url    = request.POST.get('long_url')
        short_url   = request.POST.get('short_url')
        user        = request.user

        data['long_url'] = long_url
        data['short_url'] = short_url
        data['user'] = user

        dat = CustomURLs.objects.create(
            long_url = long_url,
            short_url = short_url,
            user = user,
            )
        ser_instance = serializers.serialize('json', [dat,])
        return JsonResponse({"instance": ser_instance}, status=200)

def update(request, pk):
    link = CustomURLs.objects.get(id=pk)
    form = UpdateCustomForm(request.POST, instance=link,)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/profile/")
        else :
            form = CustomForm(request.POST, instance=link)
    context = {
        'form': form, 
        'link':link
    }
    return render(request, 'profile/edit.html', context)

def create_main(request):
    if request.user.is_authenticated :
        if request.POST.get('action') == 'post':
            long_url    = request.POST.get('long_url')
            short_url   = request.POST.get('short_url')
            user        = request.user
            dat = CustomURLs.objects.create(
                long_url = long_url,
                short_url = short_url,
                user = user,
                )
    else :
        if request.POST.get('action') == 'post':
            long_url    = request.POST.get('long_url')
            short_url   = request.POST.get('short_url')
            dat = CustomURLs.objects.create(
                long_url = long_url,
                short_url = short_url,
                )
    ser_instance = serializers.serialize('json', [dat,])
    return JsonResponse({"instance": ser_instance}, status=200)

def delete_main(request, pk):
    a = CustomURLs.objects.get(id=pk)
    if request.method == "POST":
        a.delete()
    return HttpResponseRedirect("/profile/")
 

@login_required
def edit_profile(request):
    """ Menampilkan konten pada User Profile """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user, prefix='user')
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile, prefix='profile')
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return HttpResponseRedirect(reverse("edit_profile-page"))
    else:
        u_form = UserUpdateForm(instance=request.user, prefix='user')
        p_form = ProfileUpdateForm(instance=request.user.profile, prefix='profile')

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'profile/edit_profile.html', context)

@login_required
def profile(request):
    """ Menampilkan konten pada User Profile """
    csform  = CustomForm()
    posts   = CustomURLs.objects.filter(user=request.user)
    count   = posts.count()
    top     = posts.order_by('-foll')[:2]
    cus     = sum(posts.values_list('foll', flat=True))
    total   = cus*0.5
    custom  = posts.order_by('-id')
    context = {
        'posts': posts,
        'count': count,
        'form': csform,
        'cus': cus,
        'total': total,
        'custom': custom,
        'top': top
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
            return HttpResponseRedirect(reverse('profile-page'))
    else:
        form = UserCreationForm()
    return render(request, 'auth/signup.html', {'form': form})

def home(request):
    form    = CustomForm()
    posts   = CustomURLs.objects.all()
    count   = posts.count()
    cus     = sum(posts.values_list('foll', flat=True))
    p_count = User.objects.count()
    context = {
        'form': form,
        'posts': posts,
        'count': count,
        'cus': cus,
        'prof_count': p_count,
    }
    return render(request, 'home.html', context)


def redirect_url_view(request, slug):

    try:
        shortener = CustomURLs.objects.get(short_url=slug)
        shortener.foll += 1        
        shortener.save()
        return HttpResponseRedirect(shortener.long_url)
    except:
        raise Http404('Sorry this link is broken :(')