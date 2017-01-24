from django.db import models

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
        verbose_name_plural = "Vehiculoss"

    def __str__(self):
        return u'%s' % (self.placa)

    #def get_absolute_url(self):
    #    return reverse('sector_edit',kwargs = {'pk':self.pk })

class Baterias(models.Model):
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Bateriass"

    def __str__(self):
        return u'%s' % (self.descripcion)

class VehiculoBaterias(models.Model):
    vehiculos = models.ForeignKey(Vehiculos, related_name='vehiculo_items_baterias')
    baterias = models.ForeignKey(Baterias, related_name='vehiculo_baterias')
    cantidad = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "VehiculosBateriass"

    def __str__(self):
        return u'%s' % (self.baterias)

    #def get_absolute_url(self):
    #    return reverse('sector_edit',kwargs = {'pk':self.pk })

class Cauchos(models.Model):
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Cauchoss"

    def __str__(self):
        return u'%s' % (self.descripcion)

class Rines(models.Model):
    descripcion = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Riness"

    def __str__(self):
        return u'%s' % (self.descripcion)

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
