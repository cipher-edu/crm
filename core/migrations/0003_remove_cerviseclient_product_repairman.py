# Generated by Django 4.1.7 on 2023-03-08 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cerviseclient_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cerviseclient',
            name='product_repairman',
        ),
    ]
