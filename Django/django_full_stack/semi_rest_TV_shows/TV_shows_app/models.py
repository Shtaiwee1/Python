from django.db import models
# import datetime 
from datetime import datetime




class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
# add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        title_validate_unique=Show.objects.filter(title=postData['title'])
        if len(title_validate_unique)> 0:
            errors['title_unique'] = "Show already exists!"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"
        releasedate = datetime.strptime(postData["date"], "%Y-%m-%d")
        if releasedate > datetime.now():
            errors["date"]="Release date should be in the past"
        return errors
    
        
        
    
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    desc=models.TextField()
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
