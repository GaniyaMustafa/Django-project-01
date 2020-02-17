from django import forms

class LoginForm(forms.Form):

    def atribute_form():
        style = 'border-radius: 100px'
        return style

    username= forms.CharField(widget=forms.TextInput(
        attrs={
            'style': atribute_form()
        }), max_length=255)
    password= forms.CharField(widget=forms.PasswordInput(
        attrs={
            'style': atribute_form()
        }), max_length=255)
    

