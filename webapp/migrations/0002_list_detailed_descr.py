# Generated by Django 4.2.7 on 2023-11-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='detailed_descr',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Подробное описание'),
        ),
    ]