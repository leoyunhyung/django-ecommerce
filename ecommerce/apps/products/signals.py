# Django
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Local
from ecommerce.apps.products.models import Product, ProductOption


@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
    instance.update_product_model()


@receiver(post_delete, sender=Product)
def product_post_delete(sender, instance, *args, **kwargs):
    instance.update_product_model()


@receiver(post_save, sender=ProductOption)
def product_option_post_save(sender, instance, created, **kwargs):
    if instance.option.option_group.name == 'size':
        instance.product.update(size=instance.option.name)
