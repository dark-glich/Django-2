from django import forms 
from .models import form

class register(forms.ModelForm):
    class Meta:
        model = form
        fields =[
            'first_name',
            'last_name',
            'email',
            'password',
            'terms_condition']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-data', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-data', 'placeholder': 'Enter Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-data', 'placeholder': 'Enter Email ID'}),
            'password': forms.TextInput(attrs={'class': 'form-data', 'placeholder': 'Enter Password'}),
            'terms_condition': forms.CheckboxInput(attrs={'class': "check"})
        }

    def clean_terms_condition(self, *args, **kwargs):
        name = self.cleaned_data.get('terms_condition')
        if name == True:
            return name
        else:
            raise forms.ValidationError('')
        
