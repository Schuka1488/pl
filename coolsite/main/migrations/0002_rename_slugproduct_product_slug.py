# Generated by Django 4.2.7 on 2023-11-27 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slugProduct',
            new_name='slug',
        ),
    ]
