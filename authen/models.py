from django.db import models

# Create your models here.

class hyu_users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    admission_year = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    self_introduce = models.TextField(null=True)

    def __str__(self):
        return self.user_id

