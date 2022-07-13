# Django
from django.db.models.signals import post_save
from django.dispatch import receiver

# Local
from ecommerce.apps.points.models import Point
from ecommerce.apps.users.models import User


@receiver(post_save, sender=User)
def point_post_save(sender, instance, created, **kwargs):
    if created:
        point = Point.objects.create(user=instance, name='회원 가입 이벤트', discount_price=2000)
        user_point = instance.point
        total_point = user_point + point.discount_price
        instance.update(point=total_point)
