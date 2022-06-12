from django import forms
from django.core.mail import send_mail

from locallibrary import settings
from polls.models import Customer, Movie, Video


class AddPostForm(forms.Form):
    First_name = forms.CharField(max_length=100, label = 'first name')
    Last_name = forms.CharField(max_length=100, label="last name")
    email = forms.EmailField(label="gmail")
    # photo = forms.ImageField()
    phon_number = forms.CharField(label="phone number")
    card_number = forms.CharField(max_length=50)
    address = forms.CharField(max_length=50)
    password = forms.CharField()
    money = forms.IntegerField()

    class Meta:
        model = Customer


class Id_need(forms.ModelForm):
    class Meta:
        model = Video
        fields ="__all__"
class MovieCreate(forms.ModelForm):
    class Meta:
        model = Movie
        model2 = Video
        fields = '__all__'