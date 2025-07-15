from django.db import models
class Login(models.Model):
    login_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_login"
class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address =models.TextField()
    phone_number=models.BigIntegerField(null=True)
    email=models.CharField(max_length=100,null=True)
    login=models.ForeignKey(Login,blank=True,on_delete=models.CASCADE)
    class Meta:
        db_table = 'tbl_user'


class Book(models.Model):
    bookname = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField() 
    class Meta:
        db_table = 'tbl_book'
