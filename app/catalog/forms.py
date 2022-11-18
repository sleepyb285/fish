from django import forms
from django.forms import ModelForm
from .models import Callback_request

class CallbackForm(ModelForm):
    class Meta:
        model = Callback_request
        fields = ['name','phone','email','text']
        labels = {
            'name': ('Имя*'),  
            'phone': ('Номер телефона*'),
            'email': ('E-mail'),
            'text' : ('Вопрос')
        }
    # name = forms.CharField(label='Имя*', max_length=100)
    # email =forms.EmailField(label ='E-mail', required=False)
    # phone = PhoneField()
    # body = forms.CharField(label = 'Вопрос',widget=forms.Textarea)

