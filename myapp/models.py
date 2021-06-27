from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver

# Import the function used to create random codes
from .utils import create_shortened_url

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image       = models.ImageField(default='images/default.jpg/', upload_to='upload')
    deskripsi   = models.TextField(null=True, blank=True, help_text='Deskripsi singkat Profile anda**')
    slug        = models.CharField(max_length=100, blank=True, null=True)
    buat        = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        self.slug = self.user.username
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Data-User'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class URLs(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    url         = models.URLField()
    short_url   = models.CharField(max_length=10, blank=True)
    slug        = models.CharField(max_length=100, blank=True, null=True)
    buat        = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Data-URL'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)
        self.slug = "http://127.0.0.1:8000/{}".format(self.short_url)
        super(URLs, self).save(*args, **kwargs)


class CustomURLs(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    buat        = models.DateTimeField(auto_now_add=True)
    foll        = models.PositiveIntegerField(default=0)   
    long_url    = models.URLField()
    short_url   = models.CharField(max_length=100, unique=True, blank=True )
    url         = models.CharField(max_length=100, unique=True, blank=True)
    slug        = models.CharField(max_length=100, blank=True, null=True)

    class Meta :
        verbose_name_plural = 'Data-Custom URL'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)
        self.url = "http://127.0.0.1:8000/{}".format(self.short_url)
        self.slug = self.url
        super().save(*args, **kwargs)