# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.fields import MonitorField
from phonenumber_field.modelfields import PhoneNumberField

# Local
from ecommerce.bases.models import Model
from ecommerce.modules.choices import DELIVERY_STATUS_CHOICES
from ecommerce.utils.validators import validate_international_phonenumber


class CustomPhoneNumberField(PhoneNumberField):
    default_validators = [validate_international_phonenumber]


class Delivery(Model):
    user_address = models.ForeignKey('users.UserAddress',
                                     verbose_name=_('주소지'),
                                     on_delete=models.CASCADE,
                                     related_name='deliveries'
                                     )
    name = models.CharField(_('이름'), max_length=20)
    phone = CustomPhoneNumberField(_('전화'), max_length=20)
    total_address = models.CharField(_('주소'), max_length=100)
    main_address = models.CharField(_('메인 주소'), max_length=100)
    sub_address = models.CharField(_('서브 주소'), max_length=100)
    postal_code = models.IntegerField(_('우편 번호'))
    delivery_message = models.TextField(_('배송 메시지'), null=True, blank=True)
    delivery_request = models.TextField(_('배송 요청 사항'), null=True, blank=True)
    status = models.CharField(_('배송 현황'), max_length=50, choices=DELIVERY_STATUS_CHOICES, default='ORDER_COMPLETE')
    status_changed = MonitorField(monitor='status')

    class Meta:
        verbose_name = verbose_name_plural = _('주문 그룹 배송 정보')
