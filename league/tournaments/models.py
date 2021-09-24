from django.db import models


class Player(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    pic = models.ImageField(blank=True)
    matches_played = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    #add team

    def __str__(self):
        return self.first_name + '-' + self.last_name

class Teams(models.Model):

    name = models.CharField(max_length=20)
    logo = models.ImageField(blank=True)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.name

class TournamentsList(models.Model):

    title = models.CharField(max_length=250)
    slug = models.SlugField()
    body = models.TextField(max_length=5000)
    date = models.DateField(auto_now_add=True)
    logo = models.ImageField(blank=True)
    teams = models.ManyToManyField(Teams)
    manager = models.CharField(max_length=100)

    def __str__(self):
        return self.title