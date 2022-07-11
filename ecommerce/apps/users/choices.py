# Django
from model_utils import Choices
from django.utils.translation import gettext_lazy as _

REASON_CHOICES = Choices(
    ('ETC', _('기타')),
)
