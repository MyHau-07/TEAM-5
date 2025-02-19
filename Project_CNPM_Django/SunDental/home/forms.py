from django import forms
from django.forms import ModelForm
from E_Manage.models import CommentForm
from E_Manage.models import CustomUser
from E_Manage.models import Booking
from E_Manage.models import DangKiLichNghi
from E_Manage.models import Services
from E_Manage.models import Dentist
#from E_Manage.models import CommentFormDentist
from django.contrib.auth import get_user_model

User = get_user_model()



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

# class Comment_Form_Dentist (forms.ModelForm):
#     class Meta:
#         model = CommentFormDentist
#         fields = '__all__'
#         widgets = {
#             'message': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'id': 'basic-icon-default-message',
#                 'placeholder': 'Nhập nội dung cần tư vấn',
#                 'aria-label': 'Nhập nội dung cần tư vấn',
#                 'aria-describedby': 'basic-icon-default-message2',
#                 'rows': 4
#             })
#         }


class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'name': "password",
            'placeholder': "Nhập mật khẩu",
            'aria-describedby': "password"
        })
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'name': "password_confirm",
            'placeholder': "Nhập lại mật khẩu",
            'aria-describedby': "password_confirm"
        })
    )

    class Meta:
        model = User  # Sử dụng mô hình user tùy chỉnh
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'id': "username",
                'name': "username",
                'placeholder': "Nhập tên người dùng",
                'autofocus': True
            }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'id': "email",
                'name': "email",
                'placeholder': "Nhập email của bạn"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        # Kiểm tra nếu mật khẩu không được nhập
        if not password:
            raise forms.ValidationError("Mật khẩu là bắt buộc.")

        # Kiểm tra nếu mật khẩu xác nhận không được nhập
        if not password_confirm:
            raise forms.ValidationError("Mật khẩu xác nhận là bắt buộc.")

        # Kiểm tra nếu mật khẩu và mật khẩu xác nhận không khớp
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Mật khẩu không khớp.")

        return cleaned_data
    
    
class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser 
        fields = ['full_name', 'email', 'birth_date', 'phone_number', 'address', 'gender','image']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập họ và tên'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Nhập email'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập số điện thoại'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Nhập địa chỉ', 'rows': 2}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'fullname': forms.TextInput(attrs={
                'placeholder': 'Nhập họ tên',
                'class': 'form-control'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Nhập số điện thoại',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Nhập địa chỉ email',
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'service': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.TextInput(attrs={
                'placeholder': 'Nhập tin nhắn',
                'class': 'form-control',
                'rows': 4
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'appointment_date': forms.DateInput(attrs={
                'type': 'date',  # Use HTML5 date input
                'class': 'form-control'
            }),
            'appointment_time': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }
    def save(self, commit=True, user=None):
        booking = super().save(commit=False)
        if user:
            booking.patient = user  # Gán patient là người dùng hiện tại
        if commit:
            booking.save()
        return booking


class DangKiLichNghiForm(forms.ModelForm):
    class Meta:
        model = DangKiLichNghi
        fields = ['full_name','ngay_nghi', 'ca_nghi', 'ly_do_nghi', 'mo_ta']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập họ và tên'}),
            'ngay_nghi': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ca_nghi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập ca nghỉ'}),
            'ly_do_nghi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập lý do nghỉ'}),
            'mo_ta': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mô tả chi tiết', 'rows': 3}),
        }

class ThemDichVuForm(forms.ModelForm):
    class Meta:
        model=Services
        fields=['name','price', 'info', 'image', 'time']
        widgets = {
            'name': forms.TextInput(),
            'price': forms.TextInput(),
            'info': forms.Textarea(),
            'image': forms.FileInput(),
            'time': forms.TextInput(),
        }

class SuaDichVuForm(forms.ModelForm):
    class Meta:
        model=Services
        fields=['name','price', 'info', 'image', 'time']
        widgets = {
            'name': forms.TextInput(),
            'price': forms.TextInput(),
            'info': forms.Textarea(),
            'image': forms.FileInput(),
            'time': forms.TextInput(),
        }

class DentistForm(forms.ModelForm):
    class Meta:
        model = Dentist
        fields = '__all__'
        widgets = {
            'FullName': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nguyen Van A'
            }),
            'Specialization': forms.TextInput(attrs={
                'class': 'form-control',    
                'placeholder': 'Chuyên môn nha khoa'
            }),
            'License_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Số giấy phép hành nghề'
            }),
            'Dental_branch': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Chi nhánh nha khoa'
            }),
            'Phone_Number': forms.TextInput(attrs={
                'class': 'form-control phone-mask',
                'placeholder': '+84 386699723'
            }),
            'Email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'nguyenvana@gmail.com'
            }),
            'Birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'gender': forms.Select(choices=[(True, 'Male'), (False, 'Female')], attrs={
                'class': 'form-control'
            })
        }        