# Generated by Django 5.0.2 on 2024-03-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmaps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='reports',
            field=models.IntegerField(default=0),
        ),
    ]
