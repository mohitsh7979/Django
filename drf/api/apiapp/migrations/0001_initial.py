# Generated by Django 4.1.3 on 2023-05-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apimodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('f_name', models.CharField(max_length=30)),
                ('mobile_no', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
