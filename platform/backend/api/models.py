from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here

class Prediction(models.Model):
    prediction = models.JSONField()

class Score(models.Model):
    score = models.FloatField()