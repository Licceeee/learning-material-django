# Generated by Django 3.2.3 on 2022-01-25 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_docs'),
    ]

    operations = [
        migrations.AddField(
            model_name='docs',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
