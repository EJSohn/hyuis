from django.db import models
from authen.models import hyu_users

# Create your models here.

class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)

class board(models.Model):
    post_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(category)
    user_id = models.ForeignKey(hyu_users)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_created=True)

class comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    double_comment_id = models.ForeignKey('self')
    user_id = models.ForeignKey(hyu_users)
    board_id = models.ForeignKey(board)
    created_date = models.DateTimeField(auto_created=True)
    content = models.CharField(max_length=300)




