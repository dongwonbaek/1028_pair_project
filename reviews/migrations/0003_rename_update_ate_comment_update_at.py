# Generated by Django 3.2.13 on 2022-10-27 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='update_ate',
            new_name='update_at',
        ),
    ]
