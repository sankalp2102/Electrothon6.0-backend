# Generated by Django 5.0.2 on 2024-03-09 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roadmaps', '0003_blog_blog_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_date',
        ),
    ]