from django.db import models

# Create your models here.
class userlogin(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)

class student_details(models.Model):
    user_id = models.IntegerField(default=0)
    stud_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    date_of_birth =models.CharField(max_length=255)
    address =models.CharField(max_length=255)
    email_id = models.CharField(max_length=255)
    phn_no = models.IntegerField()

class admin_details(models.Model):
    admin_name = models.CharField(max_length=255)
    designation =models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    date_of_birth = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email_id = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phn_no = models.IntegerField()
class book_details(models.Model):
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    publish_date = models.CharField(max_length=255)
    book_copies = models.IntegerField()
class book_lend_details(models.Model):
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    stud_name = models.CharField(max_length=255)
    book_taken_date = models.CharField(max_length=255)
    book_return_date = models.CharField(max_length=255)

class fine_details(models.Model):
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    stud_name = models.CharField(max_length=255)
    book_taken_date = models.CharField(max_length=255)
    book_return_date = models.CharField(max_length=255)
    fine_amt = models.IntegerField()
