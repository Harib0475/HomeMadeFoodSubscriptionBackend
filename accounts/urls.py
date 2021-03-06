from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from .views import UsersViewSet

router = DefaultRouter()

router.register('', UsersViewSet, '')

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('token-refresh/', refresh_jwt_token),
    path('token-verify/', verify_jwt_token),
    path('', include(router.urls))
]
