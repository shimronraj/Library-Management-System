# Generated by Django 4.1.1 on 2022-11-07 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0002_admin_details_book_details_book_lend_details_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_details',
            name='password',
        ),
    ]