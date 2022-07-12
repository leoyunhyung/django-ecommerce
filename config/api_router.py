# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework_nested import routers

# Local
from ecommerce.apps.products.api.views import ProductModelViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register('product-models', ProductModelViewSet)

app_name = 'api'
urlpatterns = [
                  path('', include("ecommerce.apps.users.urls")),
              ] + router.urls
