from django.contrib import admin
from article.models import Article, Comments

# Register your models here.
class CommentsInline(admin.TabularInline):
    model = Comments
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date', 'article_image']
    inlines = [CommentsInline]
    list_filter = ['article_date']

admin.site.register(Article,ArticleAdmin)
admin.site.register(Comments)