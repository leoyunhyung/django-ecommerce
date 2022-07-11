from django.urls import path

from ecommerce.apps.users.api.views import UserViewSet

app_name = "users"
urlpatterns = [
    path('login', UserViewSet.as_view({'post': 'login'})),
    path('signup', UserViewSet.as_view({'post': 'signup'})),
    path('me', UserViewSet.as_view({'get': 'me'})),
    path('withdraw', UserViewSet.as_view({'delete': 'withdraw'}))
]
