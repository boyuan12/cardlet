from django.db import models
from django.conf import settings


# Create your models here.
class Set(models.Model):
    set_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class FlashCard(models.Model):
    order = models.IntegerField() # index order
    word = models.CharField(max_length=50)
    definition = models.CharField(max_length=250)
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
