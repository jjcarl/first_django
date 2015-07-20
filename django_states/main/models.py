from django.db import models

# Create your models here.


class State(models.Model):
    abbreviation = models.CharField(max_length=2, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

    @property
    def get_a_towns(self):
        results = self.city_set.filter(city__name__startswith="A")
        return results


class StateCapital(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    state = models.OneToOneField('main.State', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'State Capital'
        verbose_name_plural = 'State Capitals'


class City(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    state = models.ForeignKey('main.State', null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
