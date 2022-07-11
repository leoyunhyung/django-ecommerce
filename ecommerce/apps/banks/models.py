# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from ecommerce.bases.models import Model
from ecommerce.modules.choices import BANK_CHOICES


class BankAccount(Model):
    user = models.ForeignKey('users.User', verbose_name=_('유저'), on_delete=models.CASCADE, related_name='user_payments')
    bank = models.CharField(_('은행'), max_length=100, choices=BANK_CHOICES, null=True, blank=True)
    account = models.IntegerField(_('계좌'))

    class Meta:
        verbose_name = verbose_name_plural = _('은행 계좌')
