# Generated by Django 2.1.3 on 2018-11-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptante', '0003_auto_20181120_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoptante',
            name='codigo',
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='run',
            field=models.CharField(help_text='Rut del Adoptante', max_length=15, primary_key=True, serialize=False),
        ),
    ]
