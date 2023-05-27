from django import forms

from core import models


# class AccountSearch(forms.Form):
#     user = forms.CharField(label='Имя пользователя', required=False, help_text='Поиск по имени пользователя', )
#     school = forms.CharField(label='Название школы', required=False, help_text='Поиск по названию школы', )
#
#     def clean(self):
#         user_name = self.cleaned_data['user']
#         school_name = self.cleaned_data['school']
#         if user_name or school_name in '''@/*#!$%^?\[]-_)+=;`~.,<>'"|''':
#             raise forms.ValidationError('Невозможные символы')
#         return


class AccountForm(forms.ModelForm):
    login = forms.CharField(label='Логин', required=True)
    password = forms.CharField(label='Пароль', required=True)

    def clean_login(self):
        login = self.cleaned_data['login']
        if login.isnumeric():
            raise forms.ValidationError('Логин не должен состоять только из чисел')
        return login

    class Meta:
        model = models.Account
        fields = '__all__'
