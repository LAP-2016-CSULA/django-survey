# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_survey'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
