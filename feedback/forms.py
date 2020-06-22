from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """Класс формы комментариев"""
    class Meta:
        model = Feedback
        fields = ("email", "text")