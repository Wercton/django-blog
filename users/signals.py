from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil
# post_save is a signal fired after an object is saved
# receiver takes the signal and perform actions based on it
@receiver(post_save, sender=User) # when a user is saved, send this signal
def criar_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


@receiver(post_save, sender=User)
def salvar_perfil(sender, instance, **kwargs):
    instance.perfil.save()
