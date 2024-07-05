from django.db import models

class Horoscope(models.Model):
    sign = models.CharField(max_length=20)
    description = models.TextField()
    start_date = models.CharField(max_length=20)  # CharField for day and month (e.g., "MM-DD")
    end_date = models.CharField(max_length=20)
    element = models.CharField(max_length=20, default='Unknown')
    color = models.CharField(max_length=20, default='Unknown')
    positive_traits = models.JSONField(default=dict, blank=True)  # Store as JSON
    negative_traits = models.JSONField(default=dict, blank=True)  # Store as JSON
    about = models.TextField(default='N/A')
    lucky_number = models.CharField(max_length=10, default='N/A')  # CharField for lucky number
    ruling_planet = models.CharField(max_length=50, default='N/A')  # CharField for ruling planet
    compatibility = models.ManyToManyField('self', blank=True)
    friends = models.ManyToManyField('self', blank=True)
    intimates = models.ManyToManyField('self', blank=True)
    def __str__(self):
        return self.sign
class Compatibility(models.Model):
    sign1 = models.CharField(max_length=20)
    sign2 = models.CharField(max_length=20)
    compatibility_score = models.IntegerField()

    def __str__(self):
        return f"{self.sign1} and {self.sign2}"