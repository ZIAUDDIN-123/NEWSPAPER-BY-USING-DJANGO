# Generated by Django 4.0.2 on 2022-02-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_alter_newspaper_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='author_name',
            field=models.CharField(max_length=50),
        ),
    ]
