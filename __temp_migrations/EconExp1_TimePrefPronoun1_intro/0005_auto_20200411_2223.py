# Generated by Django 2.2.4 on 2020-04-11 14:23

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('EconExp1_TimePrefPronoun1_intro', '0004_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='get_money_now_or_future',
            field=otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='請選擇您要今天或未來的報酬'),
        ),
    ]
