# Generated by Django 4.0.3 on 2022-05-30 07:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_employeemembership_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemembership',
            name='id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
