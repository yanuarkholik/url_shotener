from django.template.loader import render_to_string
from django.urls import reverse
from django.core import serializers
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from .forms import UserCreationForm, UserUpdateForm, ProfileUpdateForm, CustomForm
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

# def delete_main(request, pk):
#     a = CustomURLs.objects.get(id=pk)
#     if request.method == "POST":
#         a.delete()
#     return HttpResponseRedirect("/urls/")

def edit(request, pk):     
    if request.method == "POST":         
        url = get_object_or_404(CustomURLs, pk=pk)         
        form = CustomForm(request.POST, instance=url)             
        if  form.is_valid():                 
            form.save()                 
            return JsonResponse({"success": True})             
        else:                 
            print(form.errors)      
            return JsonResponse({"success": False})

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
    cus     = sum(posts.values_list('foll', flat=True))
    total   = cus*0.5

    context = {
        'posts': posts,
        'count': count,
        'form': csform,
        'cus': cus,
        'total': total,
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
    form = CustomForm()
    cus = CustomURLs.objects.order_by('id')
    context = {
        'form': form,
        'cus': cus, 
    }
    return render(request, 'home.html', context)

def save_url_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            url = CustomURLs.objects.filter(user=request.user).order_by('-id')
            data['html_url_list'] = render_to_string('profile/includes/partial_url_list.html', {
                'custom': url
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

@login_required
def update(request, pk):
     
    if request.method == 'POST':
        form = CustomForm(request.POST, instance=get_list_or_404(CustomURLs, id=pk))
    else:
        form = CustomForm(instance=url)
    return save_url_form(request, form, 'profile/includes/partial_url_update.html')


def delete_main(request, pk):
    url = get_object_or_404(CustomURLs, id=pk)
    data = dict()
    if request.method == 'POST':
        url.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        urls = CustomURLs.objects.filter(user=request.user).order_by('-id')
        data['html_url_list'] = render_to_string('profile/includes/partial_url_list.html', {
            'custom': urls
        })
    else:
        context = {'cus': url}
        data['html_form'] = render_to_string('profile/includes/partial_url_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)

def redirect_url_view(request, slug):

    try:
        shortener = CustomURLs.objects.get(short_url=slug)
        shortener.foll += 1        
        shortener.save()
        return HttpResponseRedirect(shortener.long_url)
    except:
        raise Http404('Sorry this link is broken :(')

