from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    logo_url = models.ImageField(upload_to='team_images/', max_length=255)
    club_state = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Matches(models.Model):
    first_teamname = models.ForeignKey(Team, on_delete=models.CASCADE,
                                       related_name='first_teamname', limit_choices_to={'is_active':True})
    second_teamname = models.ForeignKey(Team, on_delete=models.CASCADE,
                                        related_name='second_teamname', limit_choices_to={'is_active':True})
    match_winner = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return '{} vs {}'.format(self.first_teamname, self.second_teamname)

class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='player_images/', max_length=255)
    jersey_number = models.IntegerField()
    country = models.CharField(max_length=50)
    player_skill = models.CharField(max_length=100, choices=[('batsman', 'Batsman'), ('bowler','Bowler'), ('all-rounder','All-rounder')])
    total_matches = models.IntegerField()
    total_runs = models.IntegerField()
    highest_scores = models.IntegerField()
    fifties = models.IntegerField()
    hundreds = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, limit_choices_to={'is_active':True})
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)