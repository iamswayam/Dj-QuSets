# Generated by Django 4.0.3 on 2022-05-30 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_remove_employeemembership_membership_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemembership',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App.employee'),
        ),
    ]
