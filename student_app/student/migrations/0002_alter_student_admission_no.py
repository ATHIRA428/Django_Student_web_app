# Generated by Django 4.2.2 on 2023-06-22 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_no',
            field=models.IntegerField(unique=True),
        ),
    ]
