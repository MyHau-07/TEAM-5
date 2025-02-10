from django import forms
from django.forms import ModelForm
from E_Manage.models import CommentForm
from django.contrib.auth.models import User

class Comment_Form (forms.ModelForm):
    class Meta:
        model = CommentForm
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'basic-icon-default-fullname',
                'placeholder': 'Nguyen Van A',
                'aria-label': 'John Doe',
                'aria-describedby': 'basic-icon-default-fullname2'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'basic-icon-default-email',
                'placeholder': 'nguyenvana@gmail.com',
                'aria-label': 'nguyenvana@gmail.com',
                'aria-describedby': 'basic-icon-default-email2'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control phone-mask',
                'id': 'basic-icon-default-phone',
                'placeholder': '+84 386699723',
                'aria-label': '+84 386699723',
                'aria-describedby': 'basic-icon-default-phone2'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'basic-icon-default-message',
                'placeholder': 'Nhập nội dung cần tư vấn',
                'aria-label': 'Nhập nội dung cần tư vấn',
                'aria-describedby': 'basic-icon-default-message2',
                'rows': 4
            })
        }
        

class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'name': "password",
            'placeholder': "Enter Password",
            'aria-describedby': "password"
        })
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'name': "password_confirm",
            'placeholder': "Enter Password Confirm ",
            'aria-describedby': "password_confirm"
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'id': "username",
                'name': "username",
                'placeholder': "Enter your username",
                'autofocus': True  # 'autofocus' should be a key with a value
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'id': "email",
                'name': "email",
                'placeholder': "Enter your email"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data