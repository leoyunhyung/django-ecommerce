# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def product_list_decorator(title='', serializer=None):
    return dict(
        operation_id=_('상품 리스트 조회'),
        operation_description=_(
            '## < 상품 리스트 조회 API 입니다. > \n'
            '### 1. Try it out \n'
            '### 2. Execute \n'
        ),
        responses={200: openapi.Response(_('ok'), serializer)},
        tags=[_(f'{title}')],
    )
