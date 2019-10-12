from django import forms

class PersonForm(forms.Form):
    id  = forms.IntegerField(label='ID')