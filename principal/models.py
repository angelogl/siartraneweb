from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Cooperativas(models.Model):
    rif = models.CharField(max_length=12,unique=True) #V-09306944-3
    descripcion = models.CharField(max_length=100, help_text='Maximo 100 caracteres')
    nombre = models.TextField(max_length=100, help_text='Maximo 100 caracteres')
    direccion = models.TextField(max_length=200, help_text='Maximo 200 caracteres')
    CedRepLegal = models.CharField(max_length=9)
    NomRepLegal = models.TextField(max_length=100, help_text='Maximo 100 caracteres')    
    TelRepLegal = models.CharField(max_length=12,help_text='Maximo 12 caracteres')
    telefono1 = models.CharField(max_length=12,help_text='Maximo 12 caracteres')
    telefono2 = models.CharField(max_length=12,help_text='Maximo 12 caracteres')
    correo = models.EmailField(max_length=200,help_text='Maximo 200 caracteres')
    class Meta:
        verbose_name_plural = "Cooperativass"

    def __str__(self):
        return u'%s' % (self.nombre)

    def __unicode__(self):
        return self.nombre
    #def get_absolute_url(self):
    #    return reverse('sector_edit',kwargs = {'pk':self.pk })

class Socios(models.Model):
    cooperativa = models.ForeignKey(Cooperativas) 
    cedula = models.CharField(max_length=9,unique=True)
    apellidos = models.CharField(max_length=100, help_text='Maximo 100 caracteres')
    nombres = models.TextField(max_length=100, help_text='Maximo 100 caracteres')
    direccion = models.TextField(max_length=200, help_text='Maximo 200 caracteres')
    telefono1 = models.CharField(max_length=12,help_text='Maximo 12 caracteres')
    telefono2 = models.CharField(max_length=12,help_text='Maximo 12 caracteres')
    telefono3 = models.CharField(max_length=12,help_text='Maximo 12 caracteres')
    correo = models.EmailField(max_length=200,help_text='Maximo 200 caracteres')

    @property
    def telefonos(self):
        return self.telefono1 + ' ' + self.telefono2 + ' ' + self.telefono3

    class Meta:
        verbose_name_plural = "Socioss"

    def __str__(self):
        return u'%s, %s' % (self.apellidos,self.nombres)

    #def get_absolute_url(self):
    #    return reverse('sector_edit',kwargs = {'pk':self.pk })

class Marcas(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50, help_text='Maximo 50 caracteres')
    class Meta:
        verbose_name_plural = "Marcass"

    def __str__(self):
        return u'%s-%s' % (self.marca,self.modelo)

class Vehiculos(models.Model):
    socio = models.ForeignKey(Socios) 
    placa = models.CharField(max_length=10)
    m3 = models.CharField(max_length=9)
    MarcaModelo = models.ForeignKey(Marcas)
    GrasaChasis = models.CharField(max_length=10) 
    SerialCarroceria = models.CharField(max_length=20)
    Color = models.CharField(max_length=20)
    Ano = models.CharField(max_length=20)
    CapacidadCarga = models.CharField(max_length=10)    

    class Meta:
        verbose_name_plural = "Vehiculos"

    def __str__(self):
        return u'%s' % (self.placa)

    def get_absolute_url(self):
        return reverse('editar', kwargs={'vehiculo_id': self.id})   

class Baterias(models.Model):
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Bateriass"

    def __str__(self):
        return u'%s' % (self.descripcion)

class VehiculoBaterias(models.Model):
    vehiculos = models.ForeignKey(Vehiculos)
    baterias = models.ForeignKey(Baterias)
    cantidad = models.PositiveSmallIntegerField()

class Cauchos(models.Model):
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Cauchoss"

    def __str__(self):
        return u'%s' % (self.descripcion)

class VehiculoCauchos(models.Model):
    vehiculos = models.ForeignKey(Vehiculos)
    cauchos = models.ForeignKey(Cauchos)
    cantidad = models.PositiveSmallIntegerField()

class Rines(models.Model):
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Riness"

    def __str__(self):
        return u'%s' % (self.descripcion)

class VehiculoRines(models.Model):
    vehiculos = models.ForeignKey(Vehiculos)
    rines = models.ForeignKey(Rines)
    cantidad = models.PositiveSmallIntegerField()

class TipoAceite(models.Model):
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "TipoAceitess"

    def __str__(self):
        return u'%s' % (self.descripcion)

class Aceites(models.Model):
    tipo = models.ForeignKey(TipoAceite)    
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Aceitess"

    def __str__(self):
        return u'%s-%s' % (self.tipo,self.descripcion)

class VehiculoAceites(models.Model):
    vehiculos = models.ForeignKey(Vehiculos)
    aceites = models.ForeignKey(Aceites)
    cantidad = models.PositiveSmallIntegerField()

class TipoFiltro(models.Model):
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "TipoFiltross"

    def __str__(self):
        return u'%s' % (self.descripcion)

class Filtros(models.Model):
    tipo = models.ForeignKey(TipoFiltro)    
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Filtross"

    def __str__(self):
        return u'%s-%s' % (self.tipo,self.descripcion)

class VehiculoFiltros(models.Model):
    vehiculos = models.ForeignKey(Vehiculos)
    filtros = models.ForeignKey(Filtros)
    cantidad = models.PositiveSmallIntegerField()

class Receta(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    
    def get_absolute_url(self):
        return reverse('editar', kwargs={'receta_id': self.id})    

class Ingrediente(models.Model):
    receta = models.ForeignKey(Receta)
    descripcion = models.CharField(max_length=255)

class Instruccion(models.Model):
    receta = models.ForeignKey(Receta)
    numero = models.PositiveSmallIntegerField(help_text='Paso número')
    descripcion = models.TextField()

