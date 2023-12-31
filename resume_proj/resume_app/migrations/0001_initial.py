# Generated by Django 4.1.3 on 2023-08-30 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='other_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectives', models.CharField(max_length=300)),
                ('skills', models.CharField(max_length=100)),
                ('educations', models.CharField(max_length=100)),
                ('certificates', models.CharField(max_length=100)),
                ('hobies', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='persnol_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('pin_code', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Haryana', 'Haryana'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Bihar', 'Bihar')], max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('profile_img', models.ImageField(upload_to='media')),
            ],
        ),
    ]
