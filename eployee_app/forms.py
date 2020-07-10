from django import forms
from . models import Employee

class Eployeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields = ('Full_name','Erp_code','Position', 'Mobile_no')
        labels ={
            'Full_name':'Full Name',
            'Erp_code':'Erp Code'
        }

    def __init__(self, *args, **kwargs):
        super(Eployeeform, self).__init__( *args ,**kwargs)
        self.fields['Position'].empty_label='Select'