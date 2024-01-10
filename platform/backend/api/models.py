from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here


class Prediction(models.Model):
    user_id = models.IntegerField(default=0)
    prediction = models.JSONField()

    def __str__(self):
        return f'{self.pk} - {self.prediction}'

    # def save(self, *args, **kwargs):
    #     # Check if the primary key is not set or is a certain value
    #     if not self.id or self.id == 1:
    #         # Set a new value for the primary key
    #         self.id = 1

    #     super().save(*args, **kwargs)


class Score(models.Model):
    user_id = models.IntegerField(default=0)
    score = models.FloatField()

    def __str__(self):
        return f"{self.pk} - {self.score}"

    # def save(self, *args, **kwargs):
    #     # Check if the primary key is not set or is a certain value
    #     if not self.id or self.id == 1:
    #         # Set a new value for the primary key
    #         self.id = 1

    #     super().save(*args, **kwargs)
