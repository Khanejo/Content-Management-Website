from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from delhi_boy.models import goods

from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

        
class goodsForm(ModelForm):
    begin_date=forms.DateField(required=False)
    expiry_date=forms.DateField(required=False)
    class Meta:
        model = goods
        fields = [ 'serial_no','equipment_name','information','software_ver','begin_date','expiry_date','is_obj_under_amc','quantity',]

class dropdownForm(forms.Form):
    dropdown =forms.CharField()
