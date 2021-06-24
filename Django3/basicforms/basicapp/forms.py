from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0]!="z":
#         raise forms.ValidationError("It needs to start with z")
#  we go into name=forms.CharField(valiator=[check_for_z])

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email=forms.EmailField(label='Enter Your Email again.')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data=super.clean()
        email=all_clean_data['email']
        vemail=all_clean_data['verify_email']
        if email!=vemail:
            raise forms.ValidationError("Make Sure your emails are the same.")
    # botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher():
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Got You Bot")
    #     return botcatcher 
