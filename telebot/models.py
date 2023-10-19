from django.db import models

# Create your models here.
class TelegramSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat_id = models.CharField(max_length=200, verbose_name='Чат ІД')
    tg_message = models.TextField(verbose_name='Текст повідомлення')

    def __str__(self):
        return self.tg_chat_id

    # змінюємо імя на укр
    class Meta:
        verbose_name = 'Налаштування'
        verbose_name_plural = 'Налаштування'