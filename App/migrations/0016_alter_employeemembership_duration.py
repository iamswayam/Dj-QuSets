# Generated by Django 4.0.3 on 2022-05-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_employeemembership_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemembership',
            name='duration',
            field=models.CharField(choices=[('30', '30 Days - 1 Month'), ('90', '90 Days - 3 months'), ('180', '180 Days - 6 months'), ('365', '365 Days - 1 Year')], default='30', max_length=125),
        ),
    ]
