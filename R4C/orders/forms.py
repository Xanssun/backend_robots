from django import forms

class OrderForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=255, required=True)
    robot_serial = forms.CharField(label='Robot Serial', max_length=5, required=True)
