# Generated by Django 3.2.9 on 2021-12-22 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20211222_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='object',
            old_name='tag_list',
            new_name='name',
        ),
    ]
