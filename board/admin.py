

# Register your models here.
from django.contrib import admin
from .models import category, board, comment, imghandler

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'category_id', 'category_name')

class BoardAdmin(admin.ModelAdmin):
    list_display = ('post_id','category_id', 'user_id', 'title', 'content', 'created_date')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('parent_id', 'comment_id', 'user_id', 'board_id', 'created_date', 'content')

class imgAdmin(admin.ModelAdmin):
    list_display = ('image', 'post_id')

admin.site.register(category, CategoryAdmin)
admin.site.register(board, BoardAdmin)
admin.site.register(comment, CommentAdmin)
admin.site.register(imghandler, imgAdmin)