# Generated by Django 4.1.2 on 2023-03-09 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hms_admin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupdetails',
            old_name='fullname',
            new_name='admin_name',
        ),
    ]