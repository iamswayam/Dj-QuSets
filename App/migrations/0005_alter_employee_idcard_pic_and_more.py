# Generated by Django 4.0.3 on 2022-05-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_employee_membership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='idCard_pic',
            field=models.ImageField(blank=True, upload_to=None, verbose_name='ID card image'),
        ),
        migrations.AlterField(
            model_name='employeemembership',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]