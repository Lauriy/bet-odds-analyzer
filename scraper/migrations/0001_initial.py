# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adversary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bookie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('external_id', models.PositiveSmallIntegerField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('bookie', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='scraper.Bookie')),
                ('canonical', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='scraper.League')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_odds', models.PositiveSmallIntegerField()),
                ('away_odds', models.PositiveSmallIntegerField()),
                ('time', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('away_adversary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_matches', to='scraper.Adversary')),
                ('home_adversary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_matches', to='scraper.Adversary')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='scraper.League')),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='league',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leagues', to='scraper.Sport'),
        ),
        migrations.AddField(
            model_name='adversary',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_adversaries', to='scraper.Sport'),
        ),
    ]