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

class Feedback_newForm(ModelForm):
    class Meta:
        model = Feedback_generic
        fields = ['name','body','image']
        labels = {
            'name': ('Имя*'),  
            'body': ('Напишите отзыв'),
            'image' : ('Прикрепить изображение')
        }