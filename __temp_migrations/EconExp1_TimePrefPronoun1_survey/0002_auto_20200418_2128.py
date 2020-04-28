# Generated by Django 2.2.4 on 2020-04-18 13:28

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('EconExp1_TimePrefPronoun1_survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='class_num',
            field=otree.db.models.StringField(choices=[('0門', '0門'), ('1門', '1門'), ('2門', '2門'), ('3門', '3門'), ('4門', '4門'), ('5門', '5門'), ('超過5門', '超過5門')], max_length=10000, null=True, verbose_name='5.您修過多少門經濟學的課程'),
        ),
    ]