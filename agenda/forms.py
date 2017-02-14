from django import forms

from models import ItemAgenda


class FormItemAgenda(forms.ModelForm):
    class Meta:
        model = ItemAgenda
        fields = "__all__"





