# Generated by Django 3.2.3 on 2021-05-24 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='material.category'),
        ),
    ]
