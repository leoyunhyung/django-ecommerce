# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework_nested import routers

# Local
from ecommerce.apps.banks.api.views import BankAccountViewSet
from ecommerce.apps.carts.api.views import CartViewSet
from ecommerce.apps.clicks.api.views import ProductModelClickListViewSet, ProductModelClickCreateViewSet
from ecommerce.apps.likes.api.views import ProductModelLikeViewSet, ProductModelLikeCrudViewSet
from ecommerce.apps.orders.api.views import OrderGroupViewSet
from ecommerce.apps.products.api.views import ProductModelViewSet, ProductViewSet
from ecommerce.apps.users.api.views import UserAddressViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register('carts', CartViewSet)
router.register('user-address', UserAddressViewSet)
router.register('order-groups', OrderGroupViewSet)
router.register('bank-accounts', BankAccountViewSet)
router.register('clicks', ProductModelClickListViewSet)
router.register('likes', ProductModelLikeCrudViewSet)

# Nested Router
router.register(r'product-models', ProductModelViewSet, basename='product-models')

products_router = routers.NestedSimpleRouter(router, r'product-models', lookup='product_model')
products_router.register(r'products', ProductViewSet, basename='product-model-products')

product_model_clicks_router = routers.NestedSimpleRouter(router, r'product-models', lookup='product_model')
product_model_clicks_router.register(r'click', ProductModelClickCreateViewSet, basename='product-model-clicks')

product_model_likes_router = routers.NestedSimpleRouter(router, r'product-models', lookup='product_model')
product_model_likes_router.register(r'like', ProductModelLikeViewSet, basename='product-model-likes')

app_name = 'api'
urlpatterns = [
                  path('', include(products_router.urls)),
                  path('', include(product_model_clicks_router.urls)),
                  path('', include(product_model_likes_router.urls)),
                  path('', include("ecommerce.apps.users.urls")),
              ] + router.urls
