from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class  BOQForm(forms.ModelForm):
    class Meta:
        model=BOQ
        fields='__all__'



class  DCForm(forms.ModelForm):
    class Meta:
        model=DC
        fields='__all__'



class  RMAForm(forms.ModelForm):
    class Meta:
        model=RMA
        fields='__all__'




class  RMA_Device_Form(forms.ModelForm):
    class Meta:
        model=RMA_Device
        fields='__all__'




class  ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'



class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2','groups','is_superuser','user_permissions']


class IRForm(forms.ModelForm):
    class Meta:
        model=IR
        fields='__all__'


class COPForm(forms.ModelForm):
    class Meta:
        model=COP
        fields='__all__'

class COPFormFilter(forms.ModelForm):
    COP_Name = forms.CharField(required=False)
    Remark = forms.CharField(required=False)
    Company=models.CharField()

    class Meta:
        model=COP
        fields=['COP_Name','Remark','Company']


class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields='__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields='__all__'


class OEMForm(forms.ModelForm):
    class Meta:
        model=OEM
        fields='__all__'





"""class RmaDeviceFrom(forms.ModelForm):
    class Meta:
        model:RMA_Device
        fields='__all__'

class RmaFrom(forms.ModelForm):
    class Meta:
        model:RMA
        fields='__all__'
        """



