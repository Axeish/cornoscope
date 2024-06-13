from django.db import models

class Horoscope(models.Model):
    sign = models.CharField(max_length=20)
    description = models.TextField()
    start_date = models.CharField(max_length=5)  # CharField for day and month (e.g., "MM-DD")
    end_date = models.CharField(max_length=5)
    element = models.CharField(max_length=20, default='Unknown')
    color = models.CharField(max_length=20, default='Unknown')
    def __str__(self):
        return self.sign
class Compatibility(models.Model):
    sign1 = models.CharField(max_length=20)
    sign2 = models.CharField(max_length=20)
    compatibility_score = models.IntegerField()

    def __str__(self):
        return f"{self.sign1} and {self.sign2}"