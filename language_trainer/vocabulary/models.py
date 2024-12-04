from django.db import models
from django.contrib.auth.models import User
import iso639

# Create your models here.
class Language(models.Model):
    # Load language choices into a list of tuples
    LANGUAGES = [(code, iso639.to_name(code)) for code in iso639.langs]

    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100, blank=True)

    def clean(self):
        # Populate the name attribute in accordance to the code given
        if not self.name:
            self.name = dict(self.LANGUAGES).get(self.code)

    def __str__(self):
        return f"{self.code} {self.name}"

class Vocabulary(models.Model):
    pass


class Tag(models.Model):
    pass


class UserVocabulary(models.Model):
    pass