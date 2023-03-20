# Generated by Django 3.2 on 2023-03-12 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign_log', '0003_invitationcodes_logandsign'),
    ]

    operations = [
        migrations.AddField(
            model_name='logandsign',
            name='number_of_session',
            field=models.CharField(default='', max_length=5, verbose_name='用户届数'),
        ),
        migrations.AddField(
            model_name='logandsign',
            name='the_sector',
            field=models.CharField(default='', max_length=20, verbose_name='用户方向'),
        ),
    ]