from django.db import models
from authen.models import hyu_users

# Create your models here.

class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name


class board(models.Model):
    post_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(category)
    user_id = models.ForeignKey(hyu_users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.post_id)

class comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(hyu_users, on_delete=models.CASCADE,)
    board_id = models.ForeignKey(board, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_created=True)
    content = models.CharField(max_length=300)

class imghandler(models.Model):
    img_url = models.CharField(max_length=300)
    post_id = models.ForeignKey(board, on_delete=models.CASCADE)




