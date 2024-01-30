from django.db import models
from django.contrib.postgres.fields import JSONField

class XAI(models.Model):
    user_id = models.IntegerField(default=0)
    xai = models.JSONField() #not final type

    def __str__(self):
        return f'{self.pk} - {self.xai}'

#Score Model
class Score(models.Model):
    user_id = models.IntegerField(default=0)
    score = models.FloatField()

    def __str__(self):
        return f"{self.pk} - {self.score}"
    
#Dataset Model
class Dataset(models.Model):
    challenge_id = models.IntegerField(default=1) #do we need an id?
    dataset = models.JSONField() #not final type

    def __str__(self):
        return f"{self.pk} - {self.dataset}"

#AI Model
class AI(models.Model):
    challenge_id = models.IntegerField(default=1)
    ai = models.JSONField() #not final type
    def __str__(self):
        return f"{self.pk} - {self.ai}"
