# Generated by Django 4.0.3 on 2022-03-29 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='image',
            new_name='photos',
        ),
    ]
