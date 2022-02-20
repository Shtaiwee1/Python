from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        #characters input length error for last_name
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
            #email validation right format error    
        if not EMAIL_REGEX.match(postData['email']):                
            errors['email'] = "Invalid email address!" 
        #password confirmation error
        if postData['password'] != postData['confirm']:
            errors["confirm"] = "Passwords don't match"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        return errors
            
    def basic_validator_second(self, postData):
        errors = {}
        #email validation right format error for the login form
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_login']):                
            errors['email-login'] = "Invalid email address!"
        #password length smaller than 18 characters error
        if len(postData['password_login']) < 8:
            errors["password-login"] = "Password should be at least 8 characters"
        return errors
    
class BookManager(models.Manager):
    def basic_validator_book(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors["title"]="Title is required"
        if len(postData['desc']) < 5:
            errors["desc"] = "description should be at least 5 characters"
        return errors
        




class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()
    # liked_books = a list of books a given user likes
    # books_uploaded = a list of books uploaded by a given user
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc=models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    objects=BookManager()
    # uploaded_by = user who uploaded a given book
    # users_who_like = a list of users who like a given book

