# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('scientific_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(default='', max_length=200)),
                ('questions', models.ManyToManyField(related_name='surveys', to='survey.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Survey2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(default='', max_length=100)),
                ('species', models.ForeignKey(null=True, to='survey.Species', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('key_choice', models.ForeignKey(null=True, to='survey.Choice', related_name='survey_question', blank=True)),
                ('previous_question', models.ForeignKey(null=True, to='survey.Question', related_name='next_question', blank=True)),
                ('question', models.ForeignKey(related_name='question', to='survey.Question')),
                ('survey', models.ForeignKey(null=True, to='survey.Survey2', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='survey.Question'),
        ),
    ]
