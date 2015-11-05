# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_survey_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='questions',
            field=models.ManyToManyField(to='survey.Question', related_name='surveys'),
        ),
    ]
