# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.TextField(max_length=50)),
                ('ementa', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaOfertada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('curso', models.TextField(max_length=255)),
                ('turma', models.TextField(max_length=5)),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('professor', models.IntegerField()),
                ('disciplina', models.IntegerField()),
            ],
        ),
    ]
