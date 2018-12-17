import os
import django
from article.models import Article,Comments
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()


articles = Article.objects.all()

print(articles)







