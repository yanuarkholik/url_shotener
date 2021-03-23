from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
import pyshorteners


class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image       = models.ImageField(default='images/default.jpg/', upload_to='upload')
    deskripsi   = models.TextField(null=True, blank=True, help_text='Deskripsi singkat Profile anda**')
    buat        = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name_plural = 'Data-User'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class URLs(models.Model):
    url         = models.URLField()
    slug        = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Data-URL'

    def save(self, *args, **kwargs):
        self.shortener = pyshorteners.Shortener()
        self.slug = self.shortener.tinyurl.short(self.url)
        super(URLs, self).save(*args, **kwargs)

    
    

        