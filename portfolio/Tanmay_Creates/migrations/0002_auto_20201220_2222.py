# Generated by Django 3.1.4 on 2020-12-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tanmay_Creates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='link',
            field=models.URLField(default='/projects#'),
        ),
    ]