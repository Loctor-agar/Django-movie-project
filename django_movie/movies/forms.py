from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    # Форма отзывы
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
