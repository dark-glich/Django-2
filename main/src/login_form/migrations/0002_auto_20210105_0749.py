# Generated by Django 3.1.5 on 2021-01-05 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
    ]
