from model_utils import Choices
from django.utils.translation import gettext_lazy as _

BANK_CHOICES = Choices(
    ('KOOKMIN_BANK', _('국민은행')),
    ('WOORI_BANK', _('우리은행')),
)


QUESTION_TYPE_CHOICES = Choices(
    ('PRODUCT', _('상품')),
    ('DELIVERY', _('배송')),
    ('REFUND', _('반품')),
    ('ETC', _('기타')),
)
