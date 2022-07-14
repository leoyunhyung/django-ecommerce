from django.db.models.signals import post_save
from django.dispatch import receiver

from ecommerce.apps.clicks.models import ProductModelClick


@receiver(post_save, sender=ProductModelClick)
def product_model_click_post_save(sender, instance, created, **kwargs):
    if created:
        product_model = instance.product_model
        product_model.clicks = product_model.product_model_clicks.count()
        product_model.save()
