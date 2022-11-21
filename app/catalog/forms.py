from django import forms
from django.forms import ModelForm
from .models import Callback_request, Feedback, Feedback_generic

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

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['fish','name','body','image']
        labels = {
            'fish': ('Рыба'),
            'name': ('Имя*'),  
            'body': ('Напишите отзыв'),
            'image' : ('Прикрепить изображение')
        }
        # widgets = {
        #     'fish': forms.HiddenInput()
        # }
        #При добавлении форма не получает ключевое поле и не сохраняет ничего в БД

class Feedback_newForm(ModelForm):
    class Meta:
        model = Feedback_generic
        fields = ['name','body','image']
        labels = {
            'name': ('Имя*'),  
            'body': ('Напишите отзыв'),
            'image' : ('Прикрепить изображение')
        }