# Generated by Django 5.1.6 on 2025-02-08 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='books/', verbose_name='Загрузите обложку книги')),
                ('title', models.CharField(max_length=100, verbose_name='Укажите название книги')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Добавьте описание к книге')),
                ('price', models.PositiveIntegerField(default=300, verbose_name='Укажите цену')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('genre', models.CharField(choices=[('FICTION', 'FICTION'), ('NONFICTION', 'NONFICTION'), ('FANTASY', 'FANTASY')], max_length=20)),
                ('email', models.CharField(blank=True, max_length=100, verbose_name='Укажите почту автора')),
                ('author', models.CharField(max_length=100, verbose_name='Укажите автора')),
                ('review', models.URLField(blank=True, verbose_name='Ссылка на краткую аннотацию о книге')),
            ],
        ),
    ]
