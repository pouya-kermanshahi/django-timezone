from django import forms


class AddOrderForm(forms.Form):
    name = forms.CharField(max_length=400)
