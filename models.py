from django.db import models


#TODO protect fields with constraints 
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
