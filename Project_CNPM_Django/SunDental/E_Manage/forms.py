from django import forms
from .models import Work_Schedule

class WorkscheduleForm(forms.ModelForm):
    class Meta:
        model = Work_Schedule
        fields = '__all__'
        widgets = {
            'ID': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id-field',
                'placeholder': '01',
                'aria-label': 'ID nhân viên',
                'aria-describedby': 'id-help'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name-field',
                'placeholder': 'Nguyen Van A',
                'aria-label': 'Họ tên bác sĩ',
                'aria-describedby': 'name-help'
            }),
            'Specialty_Name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'specialty-field',
                'placeholder': 'Chuyên khoa',
                'aria-label': 'Tên chuyên khoa'
            }),
            'Work_Date': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'id': 'work-date',
                'type': 'date',
                'placeholder': 'Chọn ngày làm việc'
            }),
            'Start_Time': forms.TimeInput(format='%H:%M', attrs={
                'class': 'form-control',
                'id': 'start-time',
                'type': 'time',
                'placeholder': 'Chọn giờ bắt đầu'
            }),
            'End_Time': forms.TimeInput(format='%H:%M', attrs={
                'class': 'form-control',
                'id': 'end-time',
                'type': 'time',
                'placeholder': 'Chọn giờ kết thúc'
            })
        }
