from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from django.http.response import Http404
from django.views import generic
from article.models import Article,Comments
from django.shortcuts import render
from article.forms import CommentForm
from django.contrib import auth
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.models import User


def index(request,page_number=1):

    articles = Article.objects.all().order_by('article_date').reverse()
    current_page = Paginator(articles,3)


    context = {
        'articles': current_page.page(page_number),
        'username': auth.get_user(request).username
    }

    print(auth.get_user(request).username)

    response = render(request, 'article/article.html', context)

    response.set_cookie('page_number',page_number)

    return response


def article(request, article_id, content_comment=None):

    single_article = Article.objects.filter(id=article_id)
    comments = Comments.objects.filter(article_id=article_id)

    form = CommentForm(request.POST)
    context = {
        'output': single_article,
        'comments': comments,
        'form': form,
        'user': auth.get_user(request),
        'username': auth.get_user(request).username
    }

    if content_comment:
        context.update(content_comment)


    return render(request, 'article/single_article.html', context)


def addlike(request, article_id):
    try:
        if article_id not in request.COOKIES:

            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()

            response = redirect('/page/%s' %request.COOKIES['page_number'])
            response.set_cookie(article_id,'nolikes')

            return response
        else:

            article = Article.objects.get(id=article_id)
            article.article_likes -= 1
            article.save()
            response = redirect('/page/%s' % request.COOKIES['page_number'])
            response.delete_cookie(article_id)

            return response

    except ObjectDoesNotExist:
        raise Http404

    return redirect('/page/%s' %request.COOKIES['page_number'])

def changecomment(request, article_id, comment_id):

    if request.method == "GET":
        print(article_id)
        print(comment_id)
        change_comment = CommentForm()
        content_comment = {
            'change_comment': change_comment,
            'comment_id': comment_id
        }
        return article(request,article_id,content_comment=content_comment)
    elif request.method == "POST":
        change_comment = CommentForm(request.POST)
        if change_comment.is_valid():
            text_from_form = change_comment.save(commit=False)
            comment_needed = Comments.objects.all().get(pk = comment_id)
            comment_needed.comments_text = str(text_from_form)
            comment_needed.save()
            return redirect('article:article', article_id)

def deletecomment(request, article_id, comment_id):
    if request.method == 'GET':
        comment = Comments.objects.all().get(pk=comment_id)
        comment.delete()
        return redirect('article:article', article_id)


def addcomment(request, article_id):


    form = CommentForm(request.POST)

    if request.method == "POST" and 'limit_comments' not in request.session:
        print('Отправляем')
        if form.is_valid():
            print('Валидная форма')
            request.session.set_expiry(60)
            request.session['limit_comments'] = True
            print(request.session.get('limit_comments'))
            print(request.session.get_expiry_age())
            # Берем данные из формы(Текст комментария) при этом мы хотим обработать эти данные без записывания в БД поэтому commit=False
            text_from_form = form.save(commit=False)
            print(text_from_form)
            current_user = request.user
            article = Article.objects.get(id=article_id)

            comment = Comments.objects.create(article_id=article_id, comments_text=str(text_from_form), comments_date=timezone.now(), comments_from = current_user)
            comment.save()
        else:
            print(form.errors)

    return redirect('article:article',article_id)


