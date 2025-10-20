from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    menuitem_id = models.SmallIntegerField(default=0)
    rating = models.SmallIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)