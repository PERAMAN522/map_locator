from django import forms

from .models import Userdetails

class UserdetailForm(forms.ModelForm):
    class Meta:
        model = Userdetails
        fields = "__all__"
