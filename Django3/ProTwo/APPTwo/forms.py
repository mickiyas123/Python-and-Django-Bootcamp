from django import forms
from APPTwo.models import User
class NewUserForm(forms.ModelForm):
    # first_name=forms.CharField()
    # last_name=forms.CharField()
    # email=forms.EmailField()
    class Meta():
        model=User
        fields='__all__'