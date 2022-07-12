# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Django Rest Framework
from rest_framework.authtoken.models import Token

# Local
from ecommerce.apps.users.models import User, UserAddress
from ecommerce.utils.exception_handlers import CustomBadRequestError


@receiver(post_save, sender=User)
def user_token_post_save(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=UserAddress)
def user_address_post_save(sender, instance, created, **kwargs):
    if not instance.user.address.filter(is_default=True).exists():
        raise CustomBadRequestError(_('bad request'))

    if instance.is_default:
        instance.user.address.filter(is_default=True).exclude(id=instance.id).update(is_default=False)

    instance.user.address.filter(id=instance.id).update(
        total_address=instance.main_address + ', ' + instance.sub_address)
