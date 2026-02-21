from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import MeView

urlpatterns = [
    path("login/token/",TokenObtainPairView.as_view(),name='token-obtain-pair'),
    path("login/token/refresh/",TokenRefreshView.as_view(),name="token-refresh"),

    path("auth/me/",MeView.as_view(),name="auth-me"),
]