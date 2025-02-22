from django.db import models


class Participant(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=[
        ('junior', 'Junior'),
        ('senior', 'Senior'),
        ('elementary', 'Elementary'),
        ('lightweight', 'Lightweight'),
        ('lfr', 'LFR (Modular)'),
    ])

    def __str__(self):
        return self.full_name
    