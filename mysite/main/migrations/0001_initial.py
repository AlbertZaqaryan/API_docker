# Generated by Django 4.2.4 on 2023-08-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Car name')),
                ('price', models.PositiveIntegerField(verbose_name='Car price')),
                ('year', models.PositiveIntegerField(verbose_name='Car year')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Phone name')),
                ('price', models.PositiveIntegerField(verbose_name='Phone price')),
            ],
        ),
    ]
