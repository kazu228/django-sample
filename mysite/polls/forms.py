from django import forms

class PersonForm(forms.Form):
    id  = forms.IntegerField(label='ID')

class PersonmodelForm(forms.Form):
    name = forms.CharField(label="名前")
    age = forms.IntegerField(label="年齢")
    birthday = forms.DateField(label="誕生日")
    mail = forms.EmailField(label="メールアドレス")
    gender = forms.BooleanField(label="性別", required=False)