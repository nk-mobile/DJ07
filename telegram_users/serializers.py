from rest_framework import serializers
from .models import TelegramUser


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ['user_id', 'username']
        extra_kwargs = {
            'user_id': {'validators': []}  # Отключаем стандартные валидаторы для уникального поля
        }

    def validate_user_id(self, value):
        if TelegramUser.objects.filter(user_id=value).exists():
            raise serializers.ValidationError("Пользователь с таким ID уже существует")
        return value