from django import forms
from .models import Patmos, User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class PatmosForm(forms.ModelForm):
    fornamn = forms.CharField(max_length=255)
    efternamn = forms.CharField(max_length=255)
    personnummer = forms.CharField(max_length=15, required=False)
    adress = forms.CharField(widget=forms.Textarea, required=False)
    telefon = forms.CharField(max_length=30, required=False)
    #fodelsedatum = forms.CharField(max_length=50, required=False)
    dopdatum = forms.CharField(max_length=50, required=False)
    ankomstdatum = forms.CharField(max_length=50, required=False)
    uttrade = forms.CharField(max_length=50, required=False)
    gift_med = forms.CharField(max_length=50, required=False)
    ogift = forms.CharField(max_length=50, required=False)
    
    class Meta:
        model = Patmos
        fields = ('fornamn', 'efternamn', 'personnummer', 'adress', 'telefon', 'dopdatum', 'ankomstdatum',
                  'uttrade', 'gift_med', 'ogift')

