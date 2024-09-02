from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def good_question(self):
        return '?' in self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    

class testing1(models.Model):
    testfield = models.DecimalField(decimal_places=2, max_digits=5)
    
class testing2(models.Model):
    date_field = models.DateTimeField(
        validators=[MinValueValidator(timezone.datetime(2023, 1, 1, tzinfo=timezone.utc))]
    )