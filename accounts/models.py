from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Judge(models.Model):
    """docstring for Judge"""
    title = models.CharField(max_length=200,blank=True, null=True)
    judgename = models.ForeignKey(User, default=None,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)

    username = models.CharField(max_length=100)
    
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

class Schedule_of_events(models.Model):
    """docstring for Schedule_of_events"""
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return self.title
    
        
class Events(models.Model):
    """docstring for Events"""
    Sched_id = models.ForeignKey(Schedule_of_events, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    event_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    judgename = models.ForeignKey(Judge,on_delete=models.CASCADE,blank=True,null=True)
    num_judges = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.event_name

    
   

        
class Contestant(models.Model):
    """docstring for Conterstant"""
    Contestant_name = models.CharField(max_length=200)
    Event_Id = models.ForeignKey(Events, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return self.Contestant_name
     
class Catergory(models.Model):
    """docstring for Catergory"""
    catergory_name = models.CharField(max_length=200)
    category_scores = models.IntegerField() 
    Catergory = models.CharField(max_length=200)
    title = models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return self.catergory_name
        

class Scores(models.Model):
    """docstring for Scores"""
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    judge_id = models.ForeignKey(Judge, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True, null=True)
    constestant_id = models.ForeignKey(Contestant, on_delete=models.CASCADE)
    catergory_id = models.ForeignKey(Catergory, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    
    
        
class Reports(models.Model):
    """docstring for Reports"""
    report_type = models.CharField(max_length=200)
    Report_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200,blank=True, null=True)
    def __str__(self):
        return self.Report_name
   

class  Results(models.Model):
    """docstring for  Results"""
    
    score_id = models.ForeignKey(Scores, on_delete=models.CASCADE)

    event_Id = models.ForeignKey(Events, on_delete=models.CASCADE)
    
    catergory_id = models.ForeignKey(Catergory, on_delete=models.CASCADE)
    
    date = models.DateTimeField(timezone.now)
    
        
        
        