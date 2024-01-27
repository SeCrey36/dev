# Generated by Django 5.0.1 on 2024-01-16 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='news_title', max_length=50, verbose_name='Название')),
                ('anons', models.CharField(default='news_title', max_length=250, verbose_name='Анонс')),
                ('full_text', models.TextField(verbose_name='Полный текст')),
                ('date', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
    ]