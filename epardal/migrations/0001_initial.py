# Generated by Django 3.2.9 on 2021-11-11 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20)),
                ('height', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
