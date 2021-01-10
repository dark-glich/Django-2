# Generated by Django 3.1.5 on 2021-01-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.SmallIntegerField(max_length=2)),
                ('email', models.EmailField(max_length=245)),
                ('password', models.CharField(max_length=40)),
                ('terms_condition', models.BooleanField(default=False)),
            ],
        ),
    ]
