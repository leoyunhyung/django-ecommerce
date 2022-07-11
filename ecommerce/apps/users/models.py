# Django
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework.authtoken.models import Token
from phonenumber_field.modelfields import PhoneNumberField

# Local
from ecommerce.apps.users.choices import REASON_CHOICES
from ecommerce.bases.models import Model
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

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = verbose_name_plural = _('유저')

    def set_user_secession(self, reason):
        UserSecession.objects.create(email=self.email, name=self.name, phone=self.phone, reason=reason)
        self.delete()


class UserSecession(Model):
    email = models.EmailField(_('이메일'), null=True, blank=True)
    name = models.CharField(_('이름'), max_length=20, null=True, blank=True)
    phone = CustomPhoneNumberField(_('전화'), max_length=20, null=True, blank=True)
    reason = models.CharField(_('사유'), max_length=100, choices=REASON_CHOICES, default='ETC')

    class Meta:
        verbose_name = verbose_name_plural = _('탈퇴 유저')


class UserAddress(Model):
    user = models.ForeignKey('User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='user_address')
    name = models.CharField(_('이름'), max_length=20, null=True, blank=True)
    phone = CustomPhoneNumberField(_('전화'), max_length=20, null=True, blank=True)
    total_address = models.CharField(_('주소'), max_length=100)
    main_address = models.CharField(_('메인 주소'), max_length=100)
    sub_address = models.CharField(_('서브 주소'), max_length=100)
    postal_code = models.IntegerField(_('우편 번호'))

    class Meta:
        verbose_name = verbose_name_plural = _('주소지')
