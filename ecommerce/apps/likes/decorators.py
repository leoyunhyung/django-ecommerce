# Django
from django.utils.translation import gettext_lazy as _

# Third Party
from drf_yasg import openapi


def product_model_like_create_decorator(title='', request_body=''):
    return dict(
        operation_id=_('찜 생성'),
        operation_description=_(
            '## < 상품 모델 찜 생성 API 입니다. > \n'
            '### ★ Authorization Token 입력 ★ \n'
            '### 1. Try it out \n'
            '### 2. `id` 입력 \n'
            '### 3. Execute \n'
        ),
        request_body=request_body,
        responses={201: openapi.Response(_('created'))},
        tags=[_(f'{title}')]
    )
