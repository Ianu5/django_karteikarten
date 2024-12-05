from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    users_using_tag = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Card(models.Model):
    foreign_word = models.CharField(max_length=100)
    translation = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, related_name='tagged_word')
    users_using_word = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.foreign_word} - {self.translation}"


