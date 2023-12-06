from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(pre_save, sender=User)
def check_unique_email(sender, instance, **kwargs):
    # Check if the email is unique
    if User.objects.filter(email=instance.email).exists():
        raise ValueError('Email must be unique.')