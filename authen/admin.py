from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import hyu_users


class userAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'password', 'admission_year', 'phone_number', 'self_introduce')

admin.site.register(hyu_users, userAdmin)

