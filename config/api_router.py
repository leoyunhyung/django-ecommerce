# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework_nested import routers

# Local
from ecommerce.apps.products.api.views import ProductModelViewSet, ProductViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'product-models', ProductModelViewSet, basename='product-models')

products_router = routers.NestedSimpleRouter(router, r'product-models', lookup='product_model')
products_router.register(r'products', ProductViewSet, basename='product-model-products')

app_name = 'api'
urlpatterns = [
                  path('', include(products_router.urls)),
                  path('', include("ecommerce.apps.users.urls")),
              ] + router.urls
