# Generated by Django 3.0.8 on 2020-10-16 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NGO', '0009_foodavbl_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodavbl',
            name='created_on',
            field=models.DateTimeField(null=True),
        ),
    ]
