# Generated by Django 4.2.18 on 2025-03-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRoles', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='roles',
            field=models.ManyToManyField(related_name='users', to='userRoles.role'),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
