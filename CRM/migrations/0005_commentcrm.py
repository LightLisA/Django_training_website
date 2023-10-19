# Generated by Django 4.2.6 on 2023-10-12 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0004_statuscrm_order_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentCrm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(verbose_name='Текст коментаря')),
                ('comment_data', models.DateTimeField(auto_now=True, verbose_name='Дата створення')),
                ('comment_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM.order', verbose_name='Замовлення')),
            ],
            options={
                'verbose_name': 'Коментар',
                'verbose_name_plural': 'Коментарі',
            },
        ),
    ]
