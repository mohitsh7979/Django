# Generated by Django 4.1.3 on 2023-03-27 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0003_delete_employee_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_model',
            name='designation',
            field=models.CharField(choices=[('Sales Officer', 'Sales Officer'), ('Territory Exceutive', 'Territory Exceutive'), ('Field Assistant', 'Field Assistant'), ('General Manager', 'General Manager'), ('HR Manager', 'HR Manager'), ('Office Management Staff', 'Office Management Staff'), ('CA', 'CA'), ('Director', 'Director'), ('Desk Office Assitant', 'Desk Office Assitant')], max_length=100),
        ),
        migrations.AlterField(
            model_name='employee_model',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=100),
        ),
    ]