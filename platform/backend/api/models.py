from django.db import models
from django.contrib.postgres.fields import JSONField


class Xaimethod(models.Model):
    challenge_id = models.IntegerField(default=1)
    xai_method = models.JSONField()  # not final type

    def __str__(self):
        return f'{self.pk} - {self.xai}'

# Score Model


class Score(models.Model):
    challenge_id = models.IntegerField(default=1)
    score = models.FloatField()

    def __str__(self):
        return f"{self.pk} - {self.score}"

# Dataset Model


class Dataset(models.Model):
    challenge_id = models.IntegerField(default=1)  # do we need an id?
    dataset = models.JSONField()  # not final type
    data = models.BinaryField()

    def __str__(self):
        return f"{self.pk} - {self.dataset} - {self.data}"

# AI Model


class Mlmodel(models.Model):
    challenge_id = models.IntegerField(default=1)
    model = models.JSONField()  # not final type

    def __str__(self):
        return f"{self.pk} - {self.ai}"
