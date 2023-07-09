# Generated by Django 4.1.3 on 2022-11-29 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
                ('fname', models.CharField(max_length=100)),
                ('Dob', models.DateField()),
                ('mobile_no', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('objective', models.CharField(max_length=1000)),
                ('skill', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('work_experience', models.CharField(max_length=100)),
                ('projects', models.CharField(max_length=100)),
                ('certificates', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('intrests', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='likes',
            fields=[
                ('resume_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='myapp.resume')),
                ('myuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('like', models.IntegerField()),
            ],
            bases=('myapp.resume',),
        ),
    ]
