# Generated by Django 4.0.3 on 2022-05-30 07:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_employee_idcard_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemembership',
            name='id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
