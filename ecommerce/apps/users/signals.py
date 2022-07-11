# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Django Rest Framework
from rest_framework.authtoken.models import Token

# Local
from ecommerce.apps.users.models import User


@receiver(post_save, sender=User)
def user_token_post_save(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
