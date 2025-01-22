from django import forms
from django.contrib.auth.models import User
from .models import Subscription
from django.contrib.auth.forms import AuthenticationForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز عبور',
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تکرار رمز عبور',
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'نام کاربری',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل',
                'class': 'form-control'
            }),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('رمزهای عبور یکسان نیستند.')
        return cd['password2']


class PurchaseForm(forms.Form):
    subscription = forms.ModelChoiceField(queryset=Subscription.objects.all(), label="انتخاب اشتراک")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام کاربری',
            'class': 'form-control'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز عبور',
            'class': 'form-control'
        })
    )



