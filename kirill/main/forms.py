from django import forms
from .models import FeedBack

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'id': 'name',
                    'class': 'form-control',
                    'placeholder': 'Имя'
                    }
                ),
            'email': forms.TextInput(
                attrs={
                    'id': 'email',
                    'class': 'form-control',
                    'placeholder': 'Почта'
                    }
                ),
            'message': forms.Textarea(
                attrs={
                    'name': 'message',
                    'id': 'message',
                    'class': 'form-control',
                    'rows': '4',
                    'placeholder': 'Сообщение'
                    }
                )
        }