from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone,dateformat
from datetime import timedelta,datetime
# Create your models here.

def td_format(td_object):
    seconds = int(td_object.total_seconds())
    periods = [
        ('year',        60*60*24*365),
        ('month',       60*60*24*30),
        ('day',         60*60*24),
        ('hour',        60*60),
        ('minute',      60),
        # ('second',      1)
    ]

    strings=[]
    for period_name, period_seconds in periods:
        if seconds > period_seconds:
            period_value , seconds = divmod(seconds, period_seconds)
            has_s = 's' if period_value > 1 else ''
            strings.append("%s %s%s" % (period_value, period_name, has_s))

    return ", ".join(strings)

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    task=models.TextField(max_length=200)       
    deadline=models.DateTimeField()
    note=models.CharField(max_length=100,null=True,blank=True)
    complete=models.BooleanField(default=False)

    class Meta:
        ordering=['deadline']
    def delta(self):
        if  timezone.now()>self.deadline:
            return False
        time=self.deadline-timezone.now()
        return td_format(time)
    
    def __str__(self):
        return self.task