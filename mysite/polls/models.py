'''Models for polls app'''
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    '''Contain Questions posed'''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        '''function to determine when the question was posted'''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return str(self.question_text)



class Choice(models.Model):
    '''Choices for the questions'''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return str(self.choice_text)
    