from django import forms

from principal.models import Socios, Marcas, Baterias, Cauchos, Rines

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

# Marcas
class PrincipalMarcas():
    marca = forms.CharField(label='Marca')
    modelo = forms.CharField(label='Modelo')

    class Meta:
        model = Marcas
        fields = ['marca','modelo']

class MarcaCreate(forms.ModelForm):
    marca = forms.CharField(label='Marca',max_length=50)
    modelo = forms.CharField(label='Modelo',max_length=50)

    class Meta:
        model = Marcas
        fields = ['marca','modelo']
    
    def __init__(self, *args, **kwargs):
        super(MarcaCreate, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['marca'].widget.attrs['style'] = 'width:370px;'
        self.fields['modelo'].widget.attrs['style'] = 'width:370px;'		

class MarcaEdit(forms.ModelForm):
    marca = forms.CharField(label='Marca',max_length=50)
    modelo = forms.CharField(label='Modelo',max_length=50)

    class Meta:
        model = Marcas
        fields = ['marca','modelo']
    
    def __init__(self, *args, **kwargs):
        super(MarcaEdit, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['marca'].widget.attrs['style'] = 'width:370px;'
        self.fields['modelo'].widget.attrs['style'] = 'width:370px;'		

# Baterías
class PrincipalBaterias():
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Baterias
        fields = ['descripcion']

class BateriaCreate(forms.ModelForm):
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Baterias
        fields = ['descripcion']
    
    def __init__(self, *args, **kwargs):
        super(BateriaCreate, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'

class BateriaEdit(forms.ModelForm):
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Baterias
        fields = ['descripcion']
    
    def __init__(self, *args, **kwargs):
        super(BateriaEdit, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'

# Cauchos
class PrincipalCauchos():
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Cauchos
        fields = ['descripcion']

class CauchoCreate(forms.ModelForm):
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Cauchos
        fields = ['descripcion']
    
    def __init__(self, *args, **kwargs):
        super(CauchoCreate, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'

class CauchoEdit(forms.ModelForm):
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Cauchos
        fields = ['descripcion']
    
    def __init__(self, *args, **kwargs):
        super(CauchoEdit, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'

# Rines
class PrincipalRines():
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Rines
        fields = ['descripcion']

class RinCreate(forms.ModelForm):
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Rines
        fields = ['descripcion']
    
    def __init__(self, *args, **kwargs):
        super(RinCreate, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'

class RinEdit(forms.ModelForm):
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Rines
        fields = ['descripcion']
    
    def __init__(self, *args, **kwargs):
        super(RinEdit, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'
