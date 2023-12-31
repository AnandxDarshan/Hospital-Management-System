# Generated by Django 4.1.2 on 2023-03-22 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared_models', '0007_prescriptions_delete_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_models.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_models.patient')),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_models.prescriptions')),
            ],
        ),
    ]
