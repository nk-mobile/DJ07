from django.urls import path
from .views import TelegramUserRegisterView

urlpatterns = [
    path('register/', TelegramUserRegisterView.as_view(), name='register-user'),
]