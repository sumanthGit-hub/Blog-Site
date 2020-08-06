from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields='__all__'
        labels={
            'FullName':'Full Name',
            'Emp_Code':'Emp-Code',
        }
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['Position'].empty_label='Select'