# Generated by Django 5.0.2 on 2024-03-03 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roadmaps', '0004_blog_teamdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='created_at',
        ),
    ]
