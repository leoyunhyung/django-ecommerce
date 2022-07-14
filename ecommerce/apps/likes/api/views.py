# Django
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.translation import gettext_lazy as _

# Django Rest Framework
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

# Third Party
from drf_yasg.utils import swagger_auto_schema, no_body

# Local
from ecommerce.apps.likes.api.serializers import ProductModelLikeSerializer
from ecommerce.apps.likes.decorators import product_model_like_create_decorator
from ecommerce.apps.likes.models import ProductModelLike
from ecommerce.bases.api import mixins
from ecommerce.bases.api.viewsets import GenericViewSet
from ecommerce.utils.api.response import Response
from ecommerce.utils.decorators import token_list_decorator, token_destroy_decorator


class ProductModelLikeViewSet(mixins.CreateModelMixin,
                              GenericViewSet):
    serializers = {'default': no_body}
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return None
        queryset = ProductModelLike.objects.filter(product_model=self.kwargs['product_model_pk']).order_by('-created')
        return queryset

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(**product_model_like_create_decorator(title='상품 모델', request_body=no_body))
    def create(self, request, *args, **kwargs):
        user = request.user
        product_model_pk = kwargs['product_model_pk']
        instance = user.set_product_model_like(product_model_pk)
        return Response(
            status=status.HTTP_201_CREATED,
            code=201,
            message=_('ok'),
            data=ProductModelLikeSerializer(instance=instance).data
        )


class ProductModelLikeCrudViewSet(mixins.ListModelMixin,
                                  mixins.DestroyModelMixin,
                                  GenericViewSet):
    serializers = {'default': ProductModelLikeSerializer}
    queryset = ProductModelLike.objects.all().order_by('-created')
    filter_backends = (DjangoFilterBackend,)

    def get_permissions(self):
        if self.action in ['list']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(**token_list_decorator(title=_('찜'), serializer=ProductModelLikeSerializer))
    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = self.filter_queryset(self.get_queryset()).filter(user=user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return Response(
                status=status.HTTP_200_OK,
                code=200,
                message=_('ok'),
                data=serializer.data
            )

    @swagger_auto_schema(**token_destroy_decorator(title='찜'))
    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)
