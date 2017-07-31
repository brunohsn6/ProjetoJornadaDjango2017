# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 02:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
                ('codigo', models.CharField(max_length=30)),
                ('score', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('media', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('data_de_nascimento', models.DateField()),
                ('foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('codigo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('codigo_da_disciplina', models.CharField(max_length=6)),
                ('data_de_inserção', models.DateField(auto_now_add=True)),
                ('eletiva', models.BooleanField(default=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso')),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]