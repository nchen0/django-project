# Generated by Django 2.1.1 on 2018-09-20 00:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_personalposts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonalPosts',
            new_name='PersonalPost',
        ),
    ]