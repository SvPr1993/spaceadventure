from django import forms
from .models import KeplerUser


class KeplerUserForm(forms.ModelForm):
    class Meta:
        model = KeplerUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



