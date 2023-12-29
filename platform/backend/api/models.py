from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here


class Prediction(models.Model):
    prediction = models.JSONField()

    def __str__(self):
        return f'{self.pk} - {self.prediction}'


class Score(models.Model):
    score = models.FloatField()

    def __str__(self):
        return f"{self.pk} - {self.score}"
