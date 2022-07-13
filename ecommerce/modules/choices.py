from model_utils import Choices
from django.utils.translation import gettext_lazy as _

REASON_CHOICES = Choices(
    ('ETC', _('기타')),
)

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

PAYMENT_TYPE_CHOICES = Choices(
    ('CARD', _('카드')),
    ('ACCOUNT', _('계좌 이체')),
    ('KAKAO', _('카카오 페이')),
)

DELIVERY_STATUS_CHOICES = Choices(
    ('ORDER_COMPLETE', _('거래체결')),
    ('SEND_COMPLETE', _('발송완료')),
    ('DELIVERY_PROCESSING', _('배송 중')),
    ('DELIVERY_COMPLETE', _('배송완료')),
)

DELIVERY_MESSAGE_CHOICES = Choices(
    ('SECURITY_OFFICE', _('부재 시 경비실에 맡겨주세요')),
    ('FRONT_HOUSE', _('부재 시 집 앞에 맡겨주세요')),
    ('DIRECT_INPUT', _('직접 입력')),
)
