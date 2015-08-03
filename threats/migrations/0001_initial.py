# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField()),
                ('timestamp', models.TextField()),
                ('endpoint', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alienvaultid', models.TextField()),
            ],
            options={
                'ordering': ('alienvaultid',),
            },
        ),
        migrations.AddField(
            model_name='visit',
            name='visitor',
            field=models.ForeignKey(related_name='visits', to='threats.Visitor'),
        ),
    ]
