# Generated by Django 4.1.1 on 2022-11-08 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0008_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='email',
            new_name='emails',
        ),
        migrations.RenameField(
            model_name='emails',
            old_name='email',
            new_name='emails',
        ),
    ]
