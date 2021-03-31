from django import forms
from .models import Oltdown
from bootstrap_datepicker_plus import DateTimePickerInput

class OltDownForm(forms.ModelForm):
    class Meta:
        model = Oltdown
        fields = ('olt_name','informed_to','reason','down_self')

        widgets = {
            'uptime': DateTimePickerInput(),
            
        }

        def __init__(self, *args, **kwargs): 
            super(OltDownForm, self).__init__(*args, **kwargs)                       
            self.fields['olt_name'].disabled = True
        