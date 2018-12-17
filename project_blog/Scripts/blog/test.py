import os
import django
from datetime import datetime as dt
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()
from django.http.request import HttpRequest
from article.forms import TestForm
from article.models import Article,Comments
from django.utils.text import Truncator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from random import randrange
from django.http import request

#
# print (os.path.abspath(__file__))
#
# comments = Comments.objects.all().filter(article_id=2)
#
# articles = Article.objects.all().filter(id = 3)
# print(articles)
#
# print(comments)
#
# a3 = Article.objects.get(pk=3)
# print(a3.comments_set.values_list())
#
# single_article = Article.objects.get(id=3)
# comment = Comments.objects.all().get(id=1)
#
#
# single_article.save()
#
# print(single_article.comments_set.values_list())
#
#
# data = {
#     'text_field': 'someda',
#     'url': 'www.google.com',
#     'age': '77',
# }
#
# f = TestForm(data,initial=data)
#
# f.fields['text_field'].label = 'Her'
#
#
# smth = {'one': '1234','two': '65431'}
# if 'one' in smth:
#     print("YES")
#
# user = authenticate(username='konstantin', password='123456')
# user.first_name = 'konstantin'
# user.last_name = 'zharich'
#
# if user is not None:
#     # print('Hello ' + user.username)
#     print(user.get_full_name())
# else:
#     print('Wrong login or password')
#
#
# all_art = Article.objects.all()
#
#
# print(all_art)

comment_needed = Comments.objects.all().get(pk=14)
print(comment_needed)