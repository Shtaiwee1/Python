from django.db import models
# import datetime 
# from time import localtime , strftime
import time



class ShowManager(models.Manager):
    def basic_validator(self, postData):
        time=time.struct_time(tm_year=2022, tm_mon=2, tm_mday=15)
        errors = {}
# add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"
        if postData['date'] > time :
            errors["date"] = "The date cannot be in the future!"
        return errors
    
        
        
    
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    desc=models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
