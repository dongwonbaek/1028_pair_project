# Generated by Django 3.2.13 on 2022-10-27 07:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0006_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='like_users',
            field=models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
