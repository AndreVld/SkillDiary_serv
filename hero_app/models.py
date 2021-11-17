from django.db import models

class HeroBad(models.Model):
    phrase = models.CharField(max_length=255)


    def __str__(self):
        return self.phrase

class HeroGood(models.Model):
    phrase = models.CharField(max_length=255)

    def __str__(self):
        return self.phrase

    
