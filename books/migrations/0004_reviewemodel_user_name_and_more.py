# Generated by Django 5.1.6 on 2025-02-20 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_reviewemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewemodel',
            name='user_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reviewemodel',
            name='choice_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_book', to='books.bookmodel'),
        ),
    ]
