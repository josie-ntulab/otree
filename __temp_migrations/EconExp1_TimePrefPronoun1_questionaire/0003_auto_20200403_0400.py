# Generated by Django 2.2.4 on 2020-04-02 20:00

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('EconExp1_TimePrefPronoun1_questionaire', '0002_auto_20200403_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='decision_duration',
            field=otree.db.models.DecimalField(decimal_places=1, default=0.0, max_digits=7, null=True),
        ),
    ]