# Django
from django.urls import include, path

# Django Rest Framework
from rest_framework_nested import routers

router = routers.SimpleRouter(trailing_slash=False)

app_name = 'api'
urlpatterns = [
                  path('', include("ecommerce.apps.users.urls")),
              ] + router.urls
