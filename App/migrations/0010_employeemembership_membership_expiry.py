# Generated by Django 4.0.3 on 2022-05-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_alter_employeemembership_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemembership',
            name='membership_expiry',
            field=models.DateField(null=True),
        ),
    ]