# Generated by Django 4.0.4 on 2022-12-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_staff_notification_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_leave',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]