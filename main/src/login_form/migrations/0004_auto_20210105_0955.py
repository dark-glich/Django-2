# Generated by Django 3.1.5 on 2021-01-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_form', '0003_auto_20210105_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='terms_condition',
            field=models.BooleanField(default=True, verbose_name='I agree to terms and conditions'),
        ),
    ]
