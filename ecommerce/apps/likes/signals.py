from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from ecommerce.apps.clicks.models import ProductModelClick
from ecommerce.apps.likes.models import ProductModelLike


@receiver(post_save, sender=ProductModelLike)
def product_model_like_post_save(sender, instance, created, **kwargs):
    if created:
        instance.update_like_product_model()


@receiver(post_delete, sender=ProductModelLike)
def product_post_delete(sender, instance, *args, **kwargs):
    instance.update_like_product_model()
