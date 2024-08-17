from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    gold = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    bronze = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Medal(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    medal_type = models.CharField(max_length=10)  # 'gold', 'silver', 'bronze'

    def __str__(self):
        return f"{self.country.name} - {self.sport.name} ({self.medal_type})"

