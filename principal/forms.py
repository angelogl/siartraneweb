from django import forms

from principal.models import Socios, Marcas, Baterias, Cauchos, Rines, Aceites, TipoAceite, Filtros, TipoFiltro, Cooperativas
from principal.models import Vehiculos, VehiculoBaterias
from django.forms import ModelChoiceField

# Cooperativa
class PrincipalCooperativas():
    rif = forms.CharField(label='Rif')
    descripcion = forms.CharField(label='Descripcion')
    nombre = forms.CharField(label='Nombre')
    direccion = forms.CharField(label='Direccion')
    CedRepLegal = forms.CharField(label='Cédula Representante Legal')
    NomRepLegal = forms.CharField(label='Nombre y Apellido Representante Legal')
    TelRepLegal = forms.CharField(label='Teléfono Representante Legal')
    telefono1 = forms.CharField(label='Teléfono Oficina')
    telefono2 = forms.CharField(label='Teléfono Móvil')
    correo = forms.CharField(label='Correo')

    class Meta:
        model = Cooperativas
        fields = ['rif','descripcion','nombres']

class CooperativaCreate(forms.ModelForm):
    rif = forms.CharField(label='Rif',initial='X-00000000-0')
    descripcion = forms.CharField(label='Descripcion')
    nombre = forms.CharField(label='Nombre')
    direccion = forms.CharField(label='Direccion')
    CedRepLegal = forms.CharField(label='Cédula del Representante')
    NomRepLegal = forms.CharField(label='Nombres del Representante')
    TelRepLegal = forms.CharField(label='Teléfono del Representante')
    telefono1 = forms.CharField(label='Teléfono Oficina')
    telefono2 = forms.CharField(label='Teléfono Móvil')
    correo = forms.CharField(label='Correo')

    class Meta:
        model = Cooperativas
        fields = ['rif', 'descripcion', 'nombre','direccion', 'CedRepLegal', 'NomRepLegal','TelRepLegal', 'telefono1', 'telefono2','correo']
    
    def __init__(self, *args, **kwargs):
        super(CooperativaCreate, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['rif'].widget.attrs['style'] = 'width:150px;'
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'		
        self.fields['nombre'].widget.attrs['style'] = 'width:370px;'	
        self.fields['direccion'].widget.attrs['style'] = 'width:370px;'		
        self.fields['CedRepLegal'].widget.attrs['style'] = 'width:150px;'	
        self.fields['NomRepLegal'].widget.attrs['style'] = 'width:370px;'		
        self.fields['TelRepLegal'].widget.attrs['style'] = 'width:370px;'	
        self.fields['telefono1'].widget.attrs['style'] = 'width:370px;'		
        self.fields['telefono2'].widget.attrs['style'] = 'width:370px;'	
        self.fields['correo'].widget.attrs['style'] = 'width:370px;'		

class CooperativaEdit(forms.ModelForm):
    rif = forms.CharField(label='Rif',initial='X-00000000-0')
    descripcion = forms.CharField(label='Descripcion')
    nombre = forms.CharField(label='Nombre')
    direccion = forms.CharField(label='Direccion')
    CedRepLegal = forms.CharField(label='Cédula del Representante')
    NomRepLegal = forms.CharField(label='Nombres del Representante')
    TelRepLegal = forms.CharField(label='Teléfono del Representante')
    telefono1 = forms.CharField(label='Teléfono Oficina')
    telefono2 = forms.CharField(label='Teléfono Móvil')
    correo = forms.CharField(label='Correo')

    class Meta:
        model = Cooperativas
        fields = ['rif', 'descripcion', 'nombre','direccion', 'CedRepLegal', 'NomRepLegal','TelRepLegal', 'telefono1', 'telefono2','correo']
    
    def __init__(self, *args, **kwargs):
        super(CooperativaEdit, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['rif'].widget.attrs['style'] = 'width:150px;'
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'		
        self.fields['nombre'].widget.attrs['style'] = 'width:370px;'	
        self.fields['direccion'].widget.attrs['style'] = 'width:370px;'		
        self.fields['CedRepLegal'].widget.attrs['style'] = 'width:150px;'	
        self.fields['NomRepLegal'].widget.attrs['style'] = 'width:370px;'		
        self.fields['TelRepLegal'].widget.attrs['style'] = 'width:370px;'	
        self.fields['telefono1'].widget.attrs['style'] = 'width:370px;'		
        self.fields['telefono2'].widget.attrs['style'] = 'width:370px;'	
        self.fields['correo'].widget.attrs['style'] = 'width:370px;'		

# Socios
class PrincipalSocios():
    cedula = forms.CharField(label='Cedula')
    apellidos = forms.CharField(label='Apellidos')
    nombres = forms.CharField(label='Nombres')

    class Meta:
        model = Socios
        fields = ['cedula','apellidos','nombres']

class SocioCreate(forms.ModelForm):
    cooperativa = ModelChoiceField(queryset=Cooperativas.objects.all(), required=True, empty_label=(u'Seleciona Cooperativa'), label='Cooperativa')    
    cedula = forms.CharField(label='Cedula',initial='V00000000',max_length=9)
    apellidos = forms.CharField(label='Apellidos')
    nombres = forms.CharField(label='Nombres')
    direccion = forms.CharField(label='Dirección')
    telefono1 = forms.CharField(label='Tlf. Móvil')
    telefono2 = forms.CharField(label='Tlf. Oficina')
    telefono3 = forms.CharField(label='Tlf. Casa')
    correo = forms.CharField(label='Correo')
    
    class Meta:
        model = Socios
        fields = ['cooperativa','cedula', 'apellidos', 'nombres','direccion','telefono1','telefono2','telefono3','correo']
    
    def __init__(self, *args, **kwargs):
        super(SocioCreate, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['cooperativa'].widget.attrs['style'] = 'width:370px;'        
        self.fields['cedula'].widget.attrs['style'] = 'width:150px;'
        self.fields['apellidos'].widget.attrs['style'] = 'width:370px;'		
        self.fields['nombres'].widget.attrs['style'] = 'width:370px;'	
        self.fields['direccion'].widget.attrs['style'] = 'width:370px;'		
        self.fields['telefono1'].widget.attrs['style'] = 'width:150px;'	
        self.fields['telefono2'].widget.attrs['style'] = 'width:150px;'		
        self.fields['telefono3'].widget.attrs['style'] = 'width:150px;'	
        self.fields['correo'].widget.attrs['style'] = 'width:370px;'		

class SocioEdit(forms.ModelForm):
    cooperativa = ModelChoiceField(queryset=Cooperativas.objects.all(), required=True, empty_label=(u'Seleciona Cooperativa'), label='Cooperativa')    
    cedula = forms.CharField(label='Cedula',initial='V00000000',max_length=9)
    apellidos = forms.CharField(label='Apellidos')
    nombres = forms.CharField(label='Nombres')
    direccion = forms.CharField(label='Dirección')
    telefono1 = forms.CharField(label='Tlf. Móvil')
    telefono2 = forms.CharField(label='Tlf. Oficina')
    telefono3 = forms.CharField(label='Tlf. Casa')
    correo = forms.CharField(label='Correo')
    
    class Meta:
        model = Socios
        fields = ['cooperativa','cedula', 'apellidos', 'nombres','direccion','telefono1','telefono2','telefono3','correo']
    
    def __init__(self, *args, **kwargs):
        super(SocioEdit, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['cooperativa'].widget.attrs['style'] = 'width:370px;'        
        self.fields['cedula'].widget.attrs['style'] = 'width:150px;'
        self.fields['apellidos'].widget.attrs['style'] = 'width:370px;'		
        self.fields['nombres'].widget.attrs['style'] = 'width:370px;'	
        self.fields['direccion'].widget.attrs['style'] = 'width:370px;'		
        self.fields['telefono1'].widget.attrs['style'] = 'width:150px;'	
        self.fields['telefono2'].widget.attrs['style'] = 'width:150px;'		
        self.fields['telefono3'].widget.attrs['style'] = 'width:150px;'	
        self.fields['correo'].widget.attrs['style'] = 'width:370px;'

# Vehiculos
class PrincipalVehiculos():
    cedula = forms.CharField(label='Cedula')
    apellidos = forms.CharField(label='Apellidos')
    nombres = forms.CharField(label='Nombres')

    class Meta:
        model = Socios
        fields = ['cedula','apellidos','nombres']

class VehiculoCreate(forms.ModelForm):
    socio = ModelChoiceField(queryset=Socios.objects.all(), required=True, empty_label=(u'Socio'), label='Socio')    
    placa = forms.CharField(label='Placa',max_length=10)
    m3 = forms.CharField(label='M3')
    MarcaModelo = ModelChoiceField(queryset=Marcas.objects.all(), required=True, empty_label=(u'Marca/Modelo'), label='Marca/Modelo')
    GrasaChasis = forms.CharField(label='Grasa Chasis')
    SerialCarroceria = forms.CharField(label='Serial Carroceria')
    Color = forms.CharField(label='Color')
    Ano = forms.CharField(label='Año')
    CapacidadCarga = forms.CharField(label='Capacidad Carga')
    
    class Meta:
        model = Vehiculos
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(VehiculoCreate, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['socio'].widget.attrs['style'] = 'width:370px;'        
        self.fields['placa'].widget.attrs['style'] = 'width:150px;'
        self.fields['m3'].widget.attrs['style'] = 'width:150px;'		
        self.fields['MarcaModelo'].widget.attrs['style'] = 'width:370px;'	
        self.fields['GrasaChasis'].widget.attrs['style'] = 'width:150px;'		
        self.fields['SerialCarroceria'].widget.attrs['style'] = 'width:150px;'	
        self.fields['Color'].widget.attrs['style'] = 'width:150px;'		
        self.fields['Ano'].widget.attrs['style'] = 'width:150px;'	
        self.fields['CapacidadCarga'].widget.attrs['style'] = 'width:150px;'		

class VehiculoEdit(forms.ModelForm):
    socio = ModelChoiceField(queryset=Socios.objects.all(), required=True, empty_label=(u'Socio'), label='Socio')    
    placa = forms.CharField(label='Placa',max_length=10)
    m3 = forms.CharField(label='M3')
    MarcaModelo = ModelChoiceField(queryset=Marcas.objects.all(), required=True, empty_label=(u'Marca/Modelo'), label='Marca/Modelo')
    GrasaChasis = forms.CharField(label='Grasa Chasis')
    SerialCarroceria = forms.CharField(label='Serial Carroceria')
    Color = forms.CharField(label='Color')
    Ano = forms.CharField(label='Año')
    CapacidadCarga = forms.CharField(label='Capacidad Carga')
    
    class Meta:
        model = Vehiculos
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(VehiculoEdit, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['socio'].widget.attrs['style'] = 'width:370px;'        
        self.fields['placa'].widget.attrs['style'] = 'width:150px;'
        self.fields['m3'].widget.attrs['style'] = 'width:150px;'		
        self.fields['MarcaModelo'].widget.attrs['style'] = 'width:370px;'	
        self.fields['GrasaChasis'].widget.attrs['style'] = 'width:150px;'		
        self.fields['SerialCarroceria'].widget.attrs['style'] = 'width:150px;'	
        self.fields['Color'].widget.attrs['style'] = 'width:150px;'		
        self.fields['Ano'].widget.attrs['style'] = 'width:150px;'	
        self.fields['CapacidadCarga'].widget.attrs['style'] = 'width:150px;'
        
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

# Aceite
class PrincipalAceite():
    tipo = ModelChoiceField(queryset=TipoAceite.objects.all(), required=True, empty_label=(u'Seleciona tipo'), label='Tipo Aceite')
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Aceites
        fields = ['tipo', 'descripcion']

class AceiteCreate(forms.ModelForm):
    tipo = forms.ModelChoiceField(TipoAceite.objects.all(),label='Tipo')
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Aceites
        fields = ['tipo', 'descripcion']
    
    def __init__(self, *args, **kwargs):
        super(AceiteCreate, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['tipo'].widget.attrs['style'] = 'width:370px;'
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'				

class AceiteEdit(forms.ModelForm):
    tipo = forms.ModelChoiceField(TipoAceite.objects.all(),label='Tipo')
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Aceites
        fields = ['tipo', 'descripcion']
    
    def __init__(self, *args, **kwargs):
        super(AceiteEdit, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['tipo'].widget.attrs['style'] = 'width:370px;'
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'				

# Filtros
class PrincipalFiltro():
    tipo = ModelChoiceField(queryset=TipoFiltro.objects.all(), required=True, empty_label=(u'Seleciona tipo'), label='Tipo Filtro')
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Filtros
        fields = ['tipo', 'descripcion']

class FiltroCreate(forms.ModelForm):
    tipo = forms.ModelChoiceField(TipoFiltro.objects.all(),label='Tipo')
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Filtros
        fields = ['tipo', 'descripcion']
    
    def __init__(self, *args, **kwargs):
        super(FiltroCreate, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['tipo'].widget.attrs['style'] = 'width:370px;'
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'				

class FiltroEdit(forms.ModelForm):
    tipo = forms.ModelChoiceField(TipoFiltro.objects.all(),label='Tipo')
    descripcion = forms.CharField(label='Descripción')

    class Meta:
        model = Filtros
        fields = ['tipo', 'descripcion']
    
    def __init__(self, *args, **kwargs):
        super(FiltroEdit, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['tipo'].widget.attrs['style'] = 'width:370px;'
        self.fields['descripcion'].widget.attrs['style'] = 'width:370px;'				
