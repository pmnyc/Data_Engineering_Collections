__author__ = 'leif'
from django.contrib.auth.models import User
from django import forms
from models import Team, Rating, Demo, RATING_CHOICES


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password')


class TeamForm(forms.ModelForm):
    name = forms.CharField(label='Team Name', widget=forms.TextInput(attrs={'size':'64','maxlength':'512'}))
    logo = forms.ImageField(label='Team Logo')
    members = forms.CharField(label='Team Members',widget=forms.TextInput(attrs={'size':'128','maxlength':'512'}))
    photo = forms.ImageField(label='Photo of Team Members')


    class Meta:
        model = Team
        exclude = ('user',)


class RatingForm(forms.ModelForm):
    comment = forms.CharField(label='What do you think of this app?', widget=forms.Textarea(attrs={'rows':'5','maxlength':'512'}))
    score = forms.ChoiceField(label='How do you rate this app?', choices = RATING_CHOICES)
    class Meta:
        model = Rating
        exclude = ('rater','demo',)

class DemoForm(forms.ModelForm):

    class Meta:
        model = Demo
        exclude = ('team','rating_count','rating_sum',)
