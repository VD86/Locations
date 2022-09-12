from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import Textarea

from .models import Post, Comment



class AuthUserForm(AuthenticationForm, forms.ModelForm):
    '''Авторизация пользователя'''
    class Meta:
        model = User
        fields = ('username', 'password')


class RegisterUserForm(forms.ModelForm):
    '''Регистрация пользователя'''
    class Meta:
        model = User
        fields = ('username', 'password')
    def save(self, commit=True):
        '''Шифрование пароля, помещаем его в БД. Для сохранения пользователя'''
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
        self.fields['text'].widget = Textarea(attrs={'row':5})
