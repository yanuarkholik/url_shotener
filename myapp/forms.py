import datetime
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper


from .models import Profile, URLs, CustomURLs


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        self.helper.form_show_errors = False

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    email = forms.EmailField(
        required=False, 
        widget=forms.EmailInput(attrs={'class': 'form-control'})
        )
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        self.helper.form_show_errors = False

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
    
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper() 
        self.helper.form_show_labels = False
        self.helper.form_show_errors = False

class InputURLs(forms.ModelForm):
    class Meta:
        model = URLs
        fields = ['url',]

    def __init__(self, *args, **kwargs):
        super(InputURLs, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        self.helper.form_show_errors = False
        
class CustomForm(forms.ModelForm):
    class Meta:
        model = CustomURLs
        fields = ('long_url', 'short_url', ) 

    def __init__(self, *args, **kwargs):
        super(CustomForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

class UpdateCustomForm(forms.ModelForm):
    long_url = forms.URLField(
        required=False, 
        widget=forms.URLInput(attrs={'placeholder': 'Your new URL here'})
        )
    short_url = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Your new URL here'} )
            )
    class Meta:
        model = CustomURLs
        fields = ['long_url', 'short_url', ]

    def __init__(self, *args, **kwargs):
        super(UpdateCustomForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.html5_required = False
