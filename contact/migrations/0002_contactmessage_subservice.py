# Generated by Django 5.1.1 on 2024-10-12 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='subService',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
