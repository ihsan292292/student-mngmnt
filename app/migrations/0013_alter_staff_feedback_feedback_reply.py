# Generated by Django 4.0.4 on 2022-12-26 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_staff_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_feedback',
            name='feedback_reply',
            field=models.TextField(),
        ),
    ]
