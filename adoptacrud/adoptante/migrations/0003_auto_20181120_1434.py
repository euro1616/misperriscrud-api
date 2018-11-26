# Generated by Django 2.1.3 on 2018-11-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptante', '0002_auto_20181119_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoptante',
            name='codigo',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='run',
            field=models.CharField(help_text='Rut del Adoptante', max_length=15),
        ),
    ]