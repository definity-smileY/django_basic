import datetime

from django.db import models
from django.utils import timezone

"""
모델은 데이터 관한 단 하나의, 가장 확실한 진리의 원천입니다.
저장하는 데이터의 필수적인 필드들과 동작들을 포함하고 있습니다.
Djangosms DRY원칙을 따릅니다. 이 원칙에 따라 데이터 모델을 한곳에서 정의하고, 이것으로부터 자동으로 뭔가를 유도하는 것이 목표입니다.
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text
    
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text