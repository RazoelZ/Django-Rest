# Generated by Django 4.2.5 on 2023-10-06 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('carsId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
            ],
        ),
    ]
