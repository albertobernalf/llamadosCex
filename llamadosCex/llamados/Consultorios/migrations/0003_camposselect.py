# Generated by Django 3.2 on 2021-06-02 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Consultorios', '0002_auto_20210526_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='CamposSelect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_consultorio', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='Consultorios.consul')),
            ],
        ),
    ]
