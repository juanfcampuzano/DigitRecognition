# Generated by Django 4.0.3 on 2022-04-12 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='box_check',
            field=models.BooleanField(default=False),
        ),
    ]
