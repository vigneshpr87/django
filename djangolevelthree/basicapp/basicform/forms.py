from django import forms
from django.core import validators

def testFn(value):
    if (value[0].lower() !='z'):
        raise forms.ValidationError('Wrong start')

class Formname(forms.Form):
    name= forms.CharField(validators=[testFn])
    email= forms.EmailField()
    verify_email = forms.EmailField(label='Re Enter the email address')
    text= forms.CharField(widget=forms.Textarea)

    botcap = forms.CharField(required=False, widget=forms.HiddenInput)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Enter Correct email")