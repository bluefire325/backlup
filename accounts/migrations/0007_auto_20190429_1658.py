# Generated by Django 2.2 on 2019-04-29 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190429_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule_of_events',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
