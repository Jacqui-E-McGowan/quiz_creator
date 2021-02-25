from django.db import models
from datetime import datetime
import bcrypt

class AdminManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        check = Admin.objects.filter(email=postData['login_email'])
        if not check:
            errors['login_email'] = 'Email has not been registered'
        return errors

class Admin(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    objects = AdminManager()

class QuizManager(models.Manager):
    def quiz_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Quiz Name must have more than 2 characters"
        if len(postData['client']) < 2:
            errors['client'] = "Client must have more than 2 characters"
        if len(postData['job_number']) < 5:
            errors['job_number'] = "Job Number must be at least 5 numbers long"
        if postData['show_date'] == "":
            errors['show_date'] = "Must enter valid date"
        return errors

    def edit_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Quiz Name must have more than 2 characters"
        if len(postData['client']) < 2:
            errors['client'] = "Client must have more than 2 characters"
        if len(postData['job_number']) < 5:
            errors['job_number'] = "Job Number must be at least 5 numbers long"
        if postData['show_date'] == "":
            errors['show_date'] = "Must enter valid date"
        return errors
        
class Quiz(models.Model):
    name = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    job_number = models.CharField(max_length=255)
    show_date = models.DateField()
    message = models.TextField(null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    created_by = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    objects = QuizManager()

class QuestionManager(models.Manager):
    def question_validator(self, postData):
        errors = {}
        if len(postData['question_text']) < 1:
            errors['question_text'] = "Question field can not be blank"
        return errors

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, related_name='quiz_question', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    objects = QuestionManager()
