# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-25 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170224_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstoqueFarma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtde', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Farma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300)),
                ('cidade', models.CharField(max_length=300)),
                ('bairro', models.CharField(max_length=300)),
                ('sec_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='estoquefarma',
            name='farma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Farma'),
        ),
        migrations.AddField(
            model_name='estoquefarma',
            name='med',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Meds'),
        ),
    ]
