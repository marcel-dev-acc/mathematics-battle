from django.db import models
from datetime import datetime
from django.db.models.fields.related import ForeignKey
import pytz

# Create your models here.
class Session(models.Model):
    uuid = models.CharField(max_length=100, null=False, blank=False)
    created_on = models.DateTimeField(default=datetime.now(pytz.UTC))

class User(models.Model):
    username = models.CharField(max_length=100, null=False, blank=False)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=datetime.now(pytz.UTC))

class Question(models.Model):
    question = models.CharField(max_length=100, null=False, blank=False)
    answer = models.CharField(max_length=100, null=False, blank=False)
    correct = models.BooleanField(default=False)
    session = ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=datetime.now(pytz.UTC))