# Generated by Django 3.2 on 2021-05-26 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consul',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('conscod', models.CharField(default='', max_length=70)),
                ('adicional', models.IntegerField()),
            ],
        ),
    ]
