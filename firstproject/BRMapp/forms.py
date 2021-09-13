from django import forms

class NewBookForm(forms.Form):
    title=forms.CharField(label='Title',max_length=100)
    price=forms.FloatField(label='Price')
    author=forms.CharField(label='Author',max_length=100)
    publisher=forms.CharField(label='Publisher')

class SearchForm(forms.Form):
    title=forms.CharField(label='Title',max_length=100)

class admin(forms.Form):
    username=forms.CharField(label='username',max_length=100)
