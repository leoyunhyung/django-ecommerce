# Django
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework.authtoken.models import Token
from phonenumber_field.modelfields import PhoneNumberField

# Local
from ecommerce.apps.deliveries.models import Delivery
from ecommerce.apps.orders.models import OrderGroup, Order
from ecommerce.apps.products.api.serializers import ProductModelSerializer, ProductModelOrderSerializer
from ecommerce.apps.products.models import Product
from ecommerce.bases.models import Model
from ecommerce.modules.choices import DELIVERY_MESSAGE_CHOICES, REASON_CHOICES
from ecommerce.utils.exception_handlers import CustomBadRequestError
from ecommerce.utils.validators import validate_international_phonenumber


class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def get_or_create_user(self, email=None, password=None):
        users = self.model.objects.filter(email=email)
        is_created = False
        if users.exists():
            user = users.first()
            return user, is_created
        is_created = True
        user = self.create_user(email=email, password=password)
        return user, is_created


class CustomPhoneNumberField(PhoneNumberField):
    default_validators = [validate_international_phonenumber]


class User(AbstractUser, Model):
    email = models.EmailField(_('이메일'), unique=True, null=True, blank=True)
    name = models.CharField(_('이름'), max_length=20, null=True, blank=True)
    phone = CustomPhoneNumberField(_('전화'), max_length=20, null=True, blank=True)
    point = models.IntegerField(_('포인트'), default=0)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = verbose_name_plural = _('유저')

    def set_user_secession(self, reason):
        UserSecession.objects.create(email=self.email, name=self.name, phone=self.phone, reason=reason)
        self.delete()

    def set_order_group(self, cart, product, point, payment_type):
        order_group = OrderGroup.objects.create(user=self)
        user_address = self.address.filter(is_default=True).first()

        delivery = Delivery.objects.create(user_address=user_address,
                                           name=user_address.name,
                                           phone=user_address.phone,
                                           total_address=user_address.total_address,
                                           main_address=user_address.main_address,
                                           sub_address=user_address.sub_address,
                                           postal_code=user_address.postal_code,
                                           delivery_message=user_address.delivery_message,
                                           delivery_request=user_address.delivery_request)

        if product:
            product = Product.objects.get(id=product, is_purchased=False)
            product_model = ProductModelOrderSerializer(product.product_model).data
            order = Order.objects.create(product_model=product_model, product=product, order_group=order_group,
                                         price=product.price, user=self, code=product.code, size=product.size)
            order_group.update(total_price=order.price, payment_type=payment_type, delivery=delivery)
            product.update(is_purchased=True)
            return order_group

        if cart:
            carts = self.carts.filter(id__in=cart, is_purchased=False)
            for cart in carts:
                product_model = ProductModelOrderSerializer(cart.product.product_model).data
                order = Order.objects.create(product_model=product_model, cart=cart, order_group=order_group,
                                             price=cart.product.price, user=self, code=cart.product.code,
                                             size=cart.product.size)
                total_price = order_group.total_price + order.price
                order_group.update(total_price=total_price, payment_type=payment_type, delivery=delivery)
                cart.update(is_purchased=True)
            return order_group
        raise CustomBadRequestError('bad request')


class UserSecession(Model):
    email = models.EmailField(_('이메일'), null=True, blank=True)
    name = models.CharField(_('이름'), max_length=20, null=True, blank=True)
    phone = CustomPhoneNumberField(_('전화'), max_length=20, null=True, blank=True)
    reason = models.CharField(_('사유'), max_length=100, choices=REASON_CHOICES, default='ETC')

    class Meta:
        verbose_name = verbose_name_plural = _('탈퇴 유저')


class UserAddress(Model):
    user = models.ForeignKey('User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='address')
    name = models.CharField(_('이름'), max_length=20)
    phone = CustomPhoneNumberField(_('전화'), max_length=20)
    total_address = models.CharField(_('주소'), max_length=100)
    main_address = models.CharField(_('메인 주소'), max_length=100)
    sub_address = models.CharField(_('서브 주소'), max_length=100)
    postal_code = models.IntegerField(_('우편 번호'))
    delivery_message = models.CharField(_('배송 메시지'), choices=DELIVERY_MESSAGE_CHOICES, max_length=100,
                                        default='SECURITY_OFFICE')
    delivery_request = models.CharField(_('배송 요청 사항'), max_length=100, null=True, blank=True)
    is_default = models.BooleanField(_('기본 배송지'), default=True)

    class Meta:
        verbose_name = verbose_name_plural = _('주소지')
