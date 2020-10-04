from django.db import models

class playlist(models.Model):
    name = models.TextField()
    link = models.TextField()
    hearts = models.IntegerField()

    def getName(self):
        return self.name
    def getLink(self):
        return self.link
    def getHearts(self):
        return self.hearts


class Notebook(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()

    def getLat(self):
        return self.lat
    def getLon(self):
        return self.lon

class Page(models.Model):
    img = models.CharField()

    def getURL(self):
        return self.img