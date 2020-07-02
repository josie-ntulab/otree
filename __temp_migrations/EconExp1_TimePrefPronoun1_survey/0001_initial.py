# Generated by Django 2.2.4 on 2020-06-04 19:12

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='econexp1_timeprefpronoun1_survey_group', to='otree.Session')),
            ],
            options={
                'db_table': 'EconExp1_TimePrefPronoun1_survey_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='econexp1_timeprefpronoun1_survey_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'EconExp1_TimePrefPronoun1_survey_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('gender', otree.db.models.StringField(choices=[('男', '男'), ('女', '女'), ('不指定', '不指定')], max_length=10000, null=True, verbose_name='1.您的性別是')),
                ('bloodgroup', otree.db.models.StringField(choices=[('A型', 'A型'), ('B型', 'B型'), ('AB型', 'AB型'), ('O型', 'O型'), ('未知', '未知'), ('以上皆非', '以上皆非')], max_length=10000, null=True, verbose_name='2.您的血型是')),
                ('taiwanese', otree.db.models.StringField(choices=[('台灣本地生', '台灣本地生'), ('非台灣本地生（例如僑生、外籍交換生學生）', '非台灣本地生（例如僑生、外籍交換生學生）')], max_length=10000, null=True, verbose_name='3.您是否為台灣本地生')),
                ('econ_manage', otree.db.models.StringField(choices=[('是', '是'), ('否', '否')], max_length=10000, null=True, verbose_name='4.您是否是經濟系或管理學院的學生')),
                ('class_num', otree.db.models.StringField(choices=[('0門', '0門'), ('1門', '1門'), ('2門', '2門'), ('3門', '3門'), ('4門', '4門'), ('5門', '5門'), ('超過5門', '超過5門')], max_length=10000, null=True, verbose_name='5.您修過多少門經濟學的課程')),
                ('grade', otree.db.models.StringField(choices=[('大學部1年級', '大學部1年級'), ('大學部2年級', '大學部2年級'), ('大學部3年級', '大學部3年級'), ('大學部4年級', '大學部4年級'), ('大學部5年級以上', '大學部5年級以上'), ('碩士班學生', '碩士班學生')], max_length=10000, null=True, verbose_name='6.您的系級是')),
                ('guess', otree.db.models.LongStringField(null=True, verbose_name='7.請您猜測本實驗的目的為何')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EconExp1_TimePrefPronoun1_survey.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='econexp1_timeprefpronoun1_survey_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='econexp1_timeprefpronoun1_survey_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EconExp1_TimePrefPronoun1_survey.Subsession')),
            ],
            options={
                'db_table': 'EconExp1_TimePrefPronoun1_survey_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EconExp1_TimePrefPronoun1_survey.Subsession'),
        ),
    ]
