from django.contrib import admin
from .models import Article,Comment

# Register your models here.
class CommentLine(admin.TabularInline):
    model   =   Comment
    extra   =   0

class ArticleInline(admin.ModelAdmin):
    inlines =[CommentLine,]

admin.site.register(Article,ArticleInline)
admin.site.register(Comment)