from django import forms
from hiring.models import CustomUser
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class LoginFormWithCaptcha(AuthenticationForm):
    captcha = CaptchaField(label='Введите код с картинки')

    class Meta:
        fields = ['username', 'password', 'captcha']


class CustomUserForm(UserCreationForm):
    KNOWLEDGE_5 = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    photo = forms.ImageField(required=True)
    phone_number = forms.CharField(max_length=15, initial='+996', required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    city = forms.CharField(max_length=100, required=True)
    resume = forms.CharField(max_length=500, required=True)
    birth_date = forms.DateField(required=True)
    education = forms.CharField(max_length=200, required=True)
    knowledge_5 = forms.ChoiceField(choices=KNOWLEDGE_5, required=True)
    passport = forms.CharField(max_length=30, required=True)
    inn = forms.CharField(max_length=16, required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'photo',
            'phone_number',
            'gender',
            'city',
            'resume',
            'birth_date',
            'education',
            'knowledge_5',
            'passport',
            'inn',
        )
    
    def save(self, commit = True):
        user = super(CustomUserForm, self).save(commit=False)
        user.inn = self.cleaned_data['inn']
        if commit:
            user.save()
        return user