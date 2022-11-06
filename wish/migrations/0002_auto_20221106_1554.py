# Generated by Django 3.2 on 2022-11-06 15:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wish',
            old_name='user',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='wish',
            name='body',
        ),
        migrations.AddField(
            model_name='wish',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wish',
            name='item',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]