# Generated by Django 3.1.6 on 2021-05-05 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temperature',
            old_name='day',
            new_name='hour',
        ),
    ]
