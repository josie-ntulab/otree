# Generated by Django 2.2.4 on 2020-04-13 18:35

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='econexp1_timeprefpronoun1_intro_group', to='otree.Session')),
            ],
            options={
                'db_table': 'EconExp1_TimePrefPronoun1_intro_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('num_questions', otree.db.models.IntegerField(null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='econexp1_timeprefpronoun1_intro_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'EconExp1_TimePrefPronoun1_intro_subsession',
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
                ('waiting_period', otree.db.models.IntegerField(null=True)),
                ('gained_amount', otree.db.models.IntegerField(null=True)),
                ('treatment_pronoun_included', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('get_money_now_or_future', otree.db.models.StringField(blank=True, max_length=10000, null=True, verbose_name='請選擇您要今天或未來的報酬')),
                ('num_listen_times', otree.db.models.IntegerField(default=0, null=True)),
                ('decision_duration', otree.db.models.FloatField(default=0, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EconExp1_TimePrefPronoun1_intro.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='econexp1_timeprefpronoun1_intro_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='econexp1_timeprefpronoun1_intro_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EconExp1_TimePrefPronoun1_intro.Subsession')),
            ],
            options={
                'db_table': 'EconExp1_TimePrefPronoun1_intro_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EconExp1_TimePrefPronoun1_intro.Subsession'),
        ),
    ]
