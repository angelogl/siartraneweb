from django import forms

from principal.models import Socios

# Socios
class PrincipalSocios():
    cedula = forms.CharField(label='Cedula')
    apellidos = forms.CharField(label='Apellidos')
    nombres = forms.CharField(label='Nombres')

    class Meta:
        model = Socios
        fields = ['cedula','apellidos','nombres']

class SocioCreate(forms.ModelForm):
    cedula = forms.CharField(label='Cedula',initial='X00000000',max_length=9)
    apellidos = forms.CharField(label='Apellidos')
    nombres = forms.CharField(label='Nombres')
    
    class Meta:
        model = Socios
        fields = ['cedula', 'apellidos', 'nombres']
    
    def __init__(self, *args, **kwargs):
        super(SocioCreate, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['cedula'].widget.attrs['style'] = 'width:50px;'
        self.fields['apellidos'].widget.attrs['style'] = 'width:370px;'		
        self.fields['nombres'].widget.attrs['style'] = 'width:370px;'	

class SocioEdit(forms.ModelForm):
    cedula = forms.CharField(label='Cedula',initial='X00000000',max_length=9)
    apellidos = forms.CharField(label='Apellidos')
    nombres = forms.CharField(label='Nombres')
    
    class Meta:
        model = Socios
        fields = ['cedula', 'apellidos', 'nombres']
    
    def __init__(self, *args, **kwargs):
        super(SocioEdit, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['cedula'].widget.attrs['style'] = 'width:50px;'
        self.fields['apellidos'].widget.attrs['style'] = 'width:370px;'		
        self.fields['nombres'].widget.attrs['style'] = 'width:370px;'	

