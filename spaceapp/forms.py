from django import forms
from .models import KeplerUser


class KeplerUserForm(forms.ModelForm):
    class Meta:
        model = KeplerUser
        fields = ["user_name", "font"]
        widgets = {
            "user_name": forms.TextInput(attrs={"class": "form-select"}),
            "font": forms.Select(attrs={"class': 'form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
