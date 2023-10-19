from django.db import models


# Create your models here.
class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Назва статусу')

    def __str__(self):
        return self.status_name

    # змінюємо імя на укр
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статуси'


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Ім\'я')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Замовлення')
    comment_text = models.TextField(verbose_name='Текст коментаря')
    comment_data = models.DateTimeField(auto_now=True, verbose_name='Дата створення')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
