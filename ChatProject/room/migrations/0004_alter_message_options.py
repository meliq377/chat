# Generated by Django 4.0.6 on 2022-08-03 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_alter_message_options_alter_room_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('room',), 'verbose_name': 'message', 'verbose_name_plural': 'messages'},
        ),
    ]
