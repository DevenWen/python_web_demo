from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):
    '''
    定义 Question Model
    - 说明一下，这里的 Model 都继承自 django.db.models.Model
    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choise(models.Model):
    '''
    定义 Choise Model
    '''
    # 定义外键
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text