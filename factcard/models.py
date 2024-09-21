from django.db import models

class FactData(models.Model):
    happy_clients = models.IntegerField(default=0)
    projects_completed = models.IntegerField(default=0)
    team_members = models.IntegerField(default=0)
    earned = models.IntegerField(default=0)

    def __str__(self):
        return f"Fact Data (ID: {self.id})"