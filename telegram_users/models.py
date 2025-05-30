from django.db import models

class TelegramUser(models.Model):
    user_id = models.BigIntegerField(unique=True)  # ID пользователя в Telegram
    username = models.CharField(max_length=255, blank=True, null=True)  # Никнейм

    def __str__(self):
        return f"{self.username} ({self.user_id})"
