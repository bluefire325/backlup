# Generated by Django 2.2 on 2019-04-29 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190429_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='judge',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='judge',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]