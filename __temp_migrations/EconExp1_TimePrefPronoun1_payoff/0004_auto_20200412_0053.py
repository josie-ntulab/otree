# Generated by Django 2.2.4 on 2020-04-11 16:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('EconExp1_TimePrefPronoun1_payoff', '0003_auto_20200412_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='account_number',
            field=otree.db.models.StringField(max_length=10000, null=True, verbose_name='請輸入你的銀行帳號：'),
        ),
    ]