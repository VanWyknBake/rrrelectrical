# Generated by Django 3.1.7 on 2021-08-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0002_auto_20210803_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='link',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(max_length=200),
        ),
    ]
