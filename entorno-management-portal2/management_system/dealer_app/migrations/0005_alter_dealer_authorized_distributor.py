# Generated by Django 4.1.3 on 2023-03-24 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealer_app', '0004_remove_distributer_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='authorized_distributor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dealer_app.distributer'),
        ),
    ]
