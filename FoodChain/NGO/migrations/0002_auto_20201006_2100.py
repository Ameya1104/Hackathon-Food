# Generated by Django 3.0.8 on 2020-10-06 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='belongs',
            old_name='is_giver',
            new_name='is_donor',
        ),
    ]
