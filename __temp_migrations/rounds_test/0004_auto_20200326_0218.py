# Generated by Django 2.2.4 on 2020-03-25 18:18

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('rounds_test', '0003_auto_20200326_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='question',
            field=otree.db.models.IntegerField(choices=[[1, '一'], [2, '二'], [3, '三']], null=True, verbose_name='qestion...'),
        ),
    ]