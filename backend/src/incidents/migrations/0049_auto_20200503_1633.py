# Generated by Django 2.2.12 on 2020-05-03 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0048_auto_20200503_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipient',
            name='recipient_type',
        ),
        migrations.RemoveField(
            model_name='reporter',
            name='reporter_type',
        ),
    ]
