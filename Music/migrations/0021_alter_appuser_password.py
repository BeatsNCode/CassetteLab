# Generated by Django 5.0.3 on 2024-05-08 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0020_alter_artist_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='password',
            field=models.BinaryField(default=None, max_length=200),
        ),
    ]
