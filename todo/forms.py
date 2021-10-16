from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = (
            'title',
            'body',
            'scheduled_at',
        )
        widgets = {}
