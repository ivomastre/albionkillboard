from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Nome', max_length=100)
    inlineMaterialRadiosExample1 = forms.BooleanField(required=False)
    inlineMaterialRadiosExample2 = forms.BooleanField(required=False)
    inlineMaterialRadiosExample3 = forms.BooleanField(required=False)

