# Generated by Django 4.1.2 on 2023-03-09 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hms_admin', '0002_rename_fullname_signupdetails_admin_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupdetails',
            old_name='email',
            new_name='admin_email',
        ),
        migrations.RenameField(
            model_name='signupdetails',
            old_name='password',
            new_name='admin_password',
        ),
        migrations.RenameField(
            model_name='signupdetails',
            old_name='username',
            new_name='admin_username',
        ),
    ]
