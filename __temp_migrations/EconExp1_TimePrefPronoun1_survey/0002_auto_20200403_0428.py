# Generated by Django 2.2.4 on 2020-04-02 20:28

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('EconExp1_TimePrefPronoun1_survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='bloodgroup',
            field=otree.db.models.StringField(choices=[('A型', 'A型'), ('B型', 'B型'), ('AB型', 'AB型'), ('O型', 'O型'), ('未知', '未知'), ('以上皆非', '以上皆非')], max_length=10000, null=True, verbose_name='2.您的血型是'),
        ),
        migrations.AddField(
            model_name='player',
            name='class_num',
            field=otree.db.models.StringField(choices=[('1門', '1門'), ('2門', '2門'), ('3門', '3門'), ('4門', '4門'), ('5門', '5門'), ('超過5門', '超過5門')], max_length=10000, null=True, verbose_name='5.您修過多少門經濟學的課程'),
        ),
        migrations.AddField(
            model_name='player',
            name='econ_manage',
            field=otree.db.models.StringField(choices=[('是', '是'), ('否', '否')], max_length=10000, null=True, verbose_name='4.您是否是經濟系或管理學院的學生'),
        ),
        migrations.AddField(
            model_name='player',
            name='gender',
            field=otree.db.models.StringField(choices=[('男', '男'), ('女', '女'), ('不指定', '不指定')], max_length=10000, null=True, verbose_name='1.您的性別是'),
        ),
        migrations.AddField(
            model_name='player',
            name='grade',
            field=otree.db.models.StringField(choices=[('大學部1年級', '大學部1年級'), ('大學部2年級', '大學部2年級'), ('大學部3年級', '大學部3年級'), ('大學部4年級', '大學部4年級'), ('大學部5年級以上', '大學部5年級以上'), ('碩士班學生', '碩士班學生')], max_length=10000, null=True, verbose_name='6.您的系級是'),
        ),
        migrations.AddField(
            model_name='player',
            name='guess',
            field=otree.db.models.LongStringField(null=True, verbose_name='7.請您猜測本實驗的目的為何'),
        ),
        migrations.AddField(
            model_name='player',
            name='taiwanese',
            field=otree.db.models.StringField(choices=[('台灣本地生', '台灣本地生'), ('非台灣本地生（例如僑生、外籍交換生學生）', '非台灣本地生（例如僑生、外籍交換生學生）')], max_length=10000, null=True, verbose_name='3.您是否為台灣本地生'),
        ),
    ]