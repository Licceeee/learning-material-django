# Generated by Django 3.2.3 on 2022-01-25 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_lesson_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['my_order'], 'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AddField(
            model_name='course',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lesson',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
