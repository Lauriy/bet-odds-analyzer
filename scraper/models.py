from django.db import models


class Bookie(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Sport(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class League(models.Model):
    sport = models.ForeignKey(Sport, related_name='leagues')
    canonical = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=255)
    bookie = models.ForeignKey(Bookie, null=True, blank=True)
    external_id = models.PositiveSmallIntegerField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('bookie', 'external_id')


class Adversary(models.Model):
    sport = models.ForeignKey(Sport, related_name='all_adversaries')
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'adversaries'


class Match(models.Model):
    league = models.ForeignKey(League, related_name='matches')
    home_adversary = models.ForeignKey(Adversary, related_name='home_matches')
    away_adversary = models.ForeignKey(Adversary, related_name='away_matches')
    home_odds = models.PositiveSmallIntegerField()
    away_odds = models.PositiveSmallIntegerField()
    time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'matches'