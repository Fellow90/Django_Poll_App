import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Published Date:",auto_now_add = True,null= True, blank= True)
    def __str__(self):
        return f"Question : {self.question_text}"
    
    def wasPublishedRecently(self):
        return self.publcnDate >= timezone.now() - timezone.timedelta(days = 1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(default= "Nothing")
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f"Choice : {self.choice_text}"
    




