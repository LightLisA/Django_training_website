from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=50, verbose_name='Ціна')
    pc_description = models.CharField(max_length=200, verbose_name='Опис')

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'Ціна'
        verbose_name_plural = 'Ціни'


class PriceTable(models.Model):
    pct_title = models.CharField(max_length=200, verbose_name='Послуга')
    pct_old_price = models.CharField(max_length=200, verbose_name='Стара ціна')
    pct_new_price = models.CharField(max_length=200, verbose_name='Нова ціна')

    def __str__(self):
        return self.pct_title

    class Meta:
        verbose_name = 'Послуга'
        verbose_name_plural = 'Послуги'