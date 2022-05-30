# Generated by Django 4.0.3 on 2022-05-30 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_alter_employeemembership_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemembership',
            name='duration',
            field=models.CharField(choices=[('30 days', '30 Days - 1 Month'), ('90 days', '90 Days - 3 months'), ('180 days', '180 Days - 6 months'), ('365 days', '365 Days - 1 Year')], default='30 days', max_length=125),
        ),
    ]
