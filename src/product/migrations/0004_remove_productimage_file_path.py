# Generated by Django 4.2.3 on 2023-07-13 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productimage_file_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='file_path',
        ),
    ]