# Generated by Django 4.1.2 on 2022-11-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_stripe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='duration',
            field=models.CharField(choices=[('once', 'Once'), ('forever', 'Forever'), ('repeating', 'Repeating')], default='forever', max_length=10, verbose_name='duration'),
        ),
    ]
