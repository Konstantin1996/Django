from django import forms
from article.models import Comments

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comments
        fields = ['comments_text']


class TestForm(forms.Form):
    text_field = forms.CharField(max_length=10)
    name = forms.CharField(required=False)
    url = forms.URLField()
    age = forms.IntegerField()