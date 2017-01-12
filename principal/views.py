from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import CreateView,TemplateView,ListView,DetailView,View

from django_modalview.generic.base import ModalTemplateView
from django_modalview.generic.edit import ModalFormView,ModalCreateView,ModalUpdateView,ModalDeleteView

from django_modalview.generic.component import ModalResponse
from django_modalview.generic.component import ModalButton

from principal.forms import SocioEdit, SocioCreate
from principal.forms import MarcaEdit, MarcaCreate
from principal.forms import BateriaEdit, BateriaCreate
from principal.forms import CauchoEdit, CauchoCreate
from principal.forms import RinEdit, RinCreate
from principal.forms import AceiteEdit, AceiteCreate

from principal.models import Socios,Marcas,Baterias,Cauchos,Rines,Aceites

from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors

from django.conf import settings

# Create your views here.
class ExampleFormViewMixin(object):
    def get_context_data(self, **kwargs):
        context_data = super(ExampleFormViewMixin, self).get_context_data(**kwargs)
        context_data['title'] = self.title
        try:
            context_data['message'] = self.request.session.get('message')
            del self.request.session['message']
        except KeyError:
            pass
        return context_data

    def get_success_url(self):
        return reverse(self.success_url)

    def form_valid(self, form):
        self.request.session['message'] = _(u'Form is valid! Submitted data: %s') % smart_unicode(
            form.cleaned_data, errors='replace')
        return super(ExampleFormViewMixin, self).form_valid(form)

    def form_invalid(self, form):
        self.message = (u'Form is invalid!')
        return super(ExampleFormViewMixin, self).form_invalid(form)

# Socios
class principal_socios2(CreateView):
   #form_class = PrincipalSocios
   template_name = 'principal_socios.html'
   success_url = 'principal_socios'
   title = (u'Principal')

   def get_context_data(self, **kwargs):
       context_data = super(principal_socios, self).get_context_data(**kwargs)
       context_data['socios_list'] = self.get_socios_list()
       return context_data

   def get_socios_list(self):
        return Socios.objects.all().order_by("cedula")

# Marcas
class principal_marcas(TemplateView):
    template_name = "principal_marcas.html"
    title = "My beautiful list of books"

    def marcas(self):
        return Marcas.objects.all()

class principal_agregar_marca(ModalCreateView):

   def __init__(self, *args, **kwargs):
     super(principal_agregar_marca, self).__init__(*args, **kwargs)
     self.title = "Agregue los datos"
     self.form_class = MarcaCreate

   def form_valid(self, form, **kwargs):
     self.save(form) #When you save the form an attribute name object is created.
     self.response = ModalResponse("{obj} creado con éxito".format(obj=self.object), 'success')
     #When you call the parent method you set commit to false because you have save the object.
     return super(principal_agregar_marca, self).form_valid(form, commit=False, **kwargs)

class principal_editar_marca(ModalUpdateView):
   def __init__(self, *args, **kwargs):
     super(principal_editar_marca, self).__init__(*args, **kwargs)
     self.title = "Actualice los datos"
     self.form_class = MarcaEdit     

   def dispatch(self, request, *args, **kwargs):
     self.object = Marcas.objects.get(pk=kwargs.get('pk'))
     return super(principal_editar_marca, self).dispatch(request, *args, **kwargs)

   def form_valid(self, form, **kwargs):
     self.response  = ModalResponse("Información actualizada", "success")
     return super(principal_editar_marca, self).form_valid(form, **kwargs)

class principal_eliminar_marca(ModalDeleteView):
   def __init__(self, *args, **kwargs):
     super(principal_eliminar_marca, self).__init__(*args, **kwargs)
     self.title = "Confirme que desea eliminar"

   def dispatch(self, request, *args, **kwargs):
     # self.object = get_user_model().objects.get(pk=kwargs.get('id'))
     self.object = Marcas.objects.get(pk=kwargs.get('pk'))     
     return super(principal_eliminar_marca, self).dispatch(request, *args, **kwargs)
   
   def delete(self, request, *args, **kwargs):
     self.response = ModalResponse("Imformación eliminada", "success")
     super(principal_eliminar_marca, self).delete(request, *args, **kwargs)

# Baterias
class principal_baterias(TemplateView):
    template_name = "principal_baterias.html"
    title = "My beautiful list of books"

    def baterias(self):
        return Baterias.objects.all()

class principal_agregar_bateria(ModalCreateView):

   def __init__(self, *args, **kwargs):
     super(principal_agregar_bateria, self).__init__(*args, **kwargs)
     self.title = "Agregue los datos"
     self.form_class = BateriaCreate

   def form_valid(self, form, **kwargs):
     self.save(form) #When you save the form an attribute name object is created.
     self.response = ModalResponse("{obj} creado con éxito".format(obj=self.object), 'success')
     #When you call the parent method you set commit to false because you have save the object.
     return super(principal_agregar_bateria, self).form_valid(form, commit=False, **kwargs)

class principal_editar_bateria(ModalUpdateView):
   def __init__(self, *args, **kwargs):
     super(principal_editar_bateria, self).__init__(*args, **kwargs)
     self.title = "Actualice los datos"
     self.form_class = BateriaEdit     

   def dispatch(self, request, *args, **kwargs):
     self.object = Baterias.objects.get(pk=kwargs.get('pk'))
     return super(principal_editar_bateria, self).dispatch(request, *args, **kwargs)

   def form_valid(self, form, **kwargs):
     self.response  = ModalResponse("Información actualizada", "success")
     return super(principal_editar_bateria, self).form_valid(form, **kwargs)

class principal_eliminar_bateria(ModalDeleteView):
   def __init__(self, *args, **kwargs):
     super(principal_eliminar_bateria, self).__init__(*args, **kwargs)
     self.title = "Confirme que desea eliminar"

   def dispatch(self, request, *args, **kwargs):
     # self.object = get_user_model().objects.get(pk=kwargs.get('id'))
     self.object = Baterias.objects.get(pk=kwargs.get('pk'))     
     return super(principal_eliminar_bateria, self).dispatch(request, *args, **kwargs)
   
   def delete(self, request, *args, **kwargs):
     self.response = ModalResponse("Imformación eliminada", "success")
     super(principal_eliminar_bateria, self).delete(request, *args, **kwargs)

# Cauchos
class principal_cauchos(TemplateView):
    template_name = "principal_cauchos.html"
    title = "My beautiful list of books"

    def cauchos(self):
        return Cauchos.objects.all()

class principal_agregar_caucho(ModalCreateView):

   def __init__(self, *args, **kwargs):
     super(principal_agregar_caucho, self).__init__(*args, **kwargs)
     self.title = "Agregue los datos"
     self.form_class = CauchoCreate

   def form_valid(self, form, **kwargs):
     self.save(form) #When you save the form an attribute name object is created.
     self.response = ModalResponse("{obj} creado con éxito".format(obj=self.object), 'success')
     #When you call the parent method you set commit to false because you have save the object.
     return super(principal_agregar_caucho, self).form_valid(form, commit=False, **kwargs)

class principal_editar_caucho(ModalUpdateView):
   def __init__(self, *args, **kwargs):
     super(principal_editar_caucho, self).__init__(*args, **kwargs)
     self.title = "Actualice los datos"
     self.form_class = CauchoEdit     

   def dispatch(self, request, *args, **kwargs):
     self.object = Cauchos.objects.get(pk=kwargs.get('pk'))
     return super(principal_editar_caucho, self).dispatch(request, *args, **kwargs)

   def form_valid(self, form, **kwargs):
     self.response  = ModalResponse("Información actualizada", "success")
     return super(principal_editar_caucho, self).form_valid(form, **kwargs)

class principal_eliminar_caucho(ModalDeleteView):
   def __init__(self, *args, **kwargs):
     super(principal_eliminar_caucho, self).__init__(*args, **kwargs)
     self.title = "Confirme que desea eliminar"

   def dispatch(self, request, *args, **kwargs):
     # self.object = get_user_model().objects.get(pk=kwargs.get('id'))
     self.object = Cauchos.objects.get(pk=kwargs.get('pk'))     
     return super(principal_eliminar_caucho, self).dispatch(request, *args, **kwargs)
   
   def delete(self, request, *args, **kwargs):
     self.response = ModalResponse("Imformación eliminada", "success")
     super(principal_eliminar_caucho, self).delete(request, *args, **kwargs)

# Rines
class principal_rines(TemplateView):
    template_name = "principal_rines.html"
    title = "My beautiful list of books"

    def rines(self):
        return Rines.objects.all()

class principal_agregar_rin(ModalCreateView):

   def __init__(self, *args, **kwargs):
     super(principal_agregar_rin, self).__init__(*args, **kwargs)
     self.title = "Agregue los datos"
     self.form_class = RinCreate

   def form_valid(self, form, **kwargs):
     self.save(form) #When you save the form an attribute name object is created.
     self.response = ModalResponse("{obj} creado con éxito".format(obj=self.object), 'success')
     #When you call the parent method you set commit to false because you have save the object.
     return super(principal_agregar_rin, self).form_valid(form, commit=False, **kwargs)

class principal_editar_rin(ModalUpdateView):
   def __init__(self, *args, **kwargs):
     super(principal_editar_rin, self).__init__(*args, **kwargs)
     self.title = "Actualice los datos"
     self.form_class = RinEdit     

   def dispatch(self, request, *args, **kwargs):
     self.object = Rines.objects.get(pk=kwargs.get('pk'))
     return super(principal_editar_rin, self).dispatch(request, *args, **kwargs)

   def form_valid(self, form, **kwargs):
     self.response  = ModalResponse("Información actualizada", "success")
     return super(principal_editar_rin, self).form_valid(form, **kwargs)

class principal_eliminar_rin(ModalDeleteView):
   def __init__(self, *args, **kwargs):
     super(principal_eliminar_rin, self).__init__(*args, **kwargs)
     self.title = "Confirme que desea eliminar"

   def dispatch(self, request, *args, **kwargs):
     # self.object = get_user_model().objects.get(pk=kwargs.get('id'))
     self.object = Rines.objects.get(pk=kwargs.get('pk'))     
     return super(principal_eliminar_rin, self).dispatch(request, *args, **kwargs)
   
   def delete(self, request, *args, **kwargs):
     self.response = ModalResponse("Imformación eliminada", "success")
     super(principal_eliminar_rin, self).delete(request, *args, **kwargs)

# Aceite
class principal_aceites(TemplateView):
    template_name = "principal_aceites.html"
    title = "My beautiful list of books"

    def aceites(self):
        return Aceites.objects.all()

class principal_agregar_aceite(ModalCreateView):

   def __init__(self, *args, **kwargs):
     super(principal_agregar_aceite, self).__init__(*args, **kwargs)
     self.title = "Agregue los datos"
     self.form_class = AceiteCreate

   def form_valid(self, form, **kwargs):
     self.save(form) #When you save the form an attribute name object is created.
     self.response = ModalResponse("{obj} creado con éxito".format(obj=self.object), 'success')
     #When you call the parent method you set commit to false because you have save the object.
     return super(principal_agregar_aceite, self).form_valid(form, commit=False, **kwargs)

class principal_editar_aceite(ModalUpdateView):
   def __init__(self, *args, **kwargs):
     super(principal_editar_aceite, self).__init__(*args, **kwargs)
     self.title = "Actualice los datos"
     self.form_class = AceiteEdit     

   def dispatch(self, request, *args, **kwargs):
     self.object = Aceites.objects.get(pk=kwargs.get('pk'))
     return super(principal_editar_aceite, self).dispatch(request, *args, **kwargs)

   def form_valid(self, form, **kwargs):
     self.response  = ModalResponse("Información actualizada", "success")
     return super(principal_editar_aceite, self).form_valid(form, **kwargs)

class principal_eliminar_aceite(ModalDeleteView):
   def __init__(self, *args, **kwargs):
     super(principal_eliminar_aceite, self).__init__(*args, **kwargs)
     self.title = "Confirme que desea eliminar"

   def dispatch(self, request, *args, **kwargs):
     # self.object = get_user_model().objects.get(pk=kwargs.get('id'))
     self.object = Aceites.objects.get(pk=kwargs.get('pk'))     
     return super(principal_eliminar_aceite, self).dispatch(request, *args, **kwargs)
   
   def delete(self, request, *args, **kwargs):
     self.response = ModalResponse("Imformación eliminada", "success")
     super(principal_eliminar_aceite, self).delete(request, *args, **kwargs)

class principal(TemplateView):
    template_name = "principal.html"
    title = "My beautiful list of books"

    def socios(self):
        return Socios.objects.all()

# Socios
class principal_socios(TemplateView):
    template_name = "principal_socios.html"
    title = "My beautiful list of books"

    def socios(self):
        return Socios.objects.all()

class principal_agregar_socio(ModalCreateView):

   def __init__(self, *args, **kwargs):
     super(principal_agregar_socio, self).__init__(*args, **kwargs)
     self.title = "Agregue los datos"
     self.form_class = SocioCreate

   def form_valid(self, form, **kwargs):
     self.save(form) #When you save the form an attribute name object is created.
     self.response = ModalResponse("{obj} creado con éxito".format(obj=self.object), 'success')
     #When you call the parent method you set commit to false because you have save the object.
     return super(principal_agregar_socio, self).form_valid(form, commit=False, **kwargs)

class principal_editar_socio(ModalUpdateView):
   def __init__(self, *args, **kwargs):
     super(principal_editar_socio, self).__init__(*args, **kwargs)
     self.title = "Actualice los datos"
     self.form_class = SocioEdit     

   def dispatch(self, request, *args, **kwargs):
     self.object = Socios.objects.get(pk=kwargs.get('pk'))
     return super(principal_editar_socio, self).dispatch(request, *args, **kwargs)

   def form_valid(self, form, **kwargs):
     self.response  = ModalResponse("Información actualizada", "success")
     return super(principal_editar_socio, self).form_valid(form, **kwargs)

class principal_eliminar_socio(ModalDeleteView):
   def __init__(self, *args, **kwargs):
     super(principal_eliminar_socio, self).__init__(*args, **kwargs)
     self.title = "Confirme que desea eliminar"

   def dispatch(self, request, *args, **kwargs):
     # self.object = get_user_model().objects.get(pk=kwargs.get('id'))
     self.object = Socios.objects.get(pk=kwargs.get('pk'))     
     return super(principal_eliminar_socio, self).dispatch(request, *args, **kwargs)
   
   def delete(self, request, *args, **kwargs):
     self.response = ModalResponse("Imformación eliminada", "success")
     super(principal_eliminar_socio, self).delete(request, *args, **kwargs)


class ReportePersonasPDF(View):  
     
    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.STATIC_ROOT+'/images/cuvolene.png'
        #archivo_imagen = 'static/images/cuvolene.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
        
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u"LISTADO DE SOCIOS")

    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Cedula', 'Apellidos', 'Nombres', 'Direccion')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(socios.cedula, socios.apellidos, socios.nombres, socios.direccion) for socios in Socios.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60,y)

    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y = 670
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

class ReporteMarcasPDF(View):  
     
    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.STATIC_ROOT+'/images/cuvolene.png'
        #archivo_imagen = 'static/images/cuvolene.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
        
        #Establecemos el tamaño de letra en 16 y el tipo de letra Helvetica
        pdf.setFont("Helvetica", 16)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(230, 790, u"LISTADO DE MARCAS")
        
    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para nuestra tabla
        encabezados = ('Marca', 'Modelo')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(marcas.marca, marcas.modelo) for marcas in Marcas.objects.all().order_by('marca')]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[8 * cm, 8 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(1,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (1, 0), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60,y)

    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y = 670
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

class ReporteBateriasPDF(View):  
     
    def cabecera(self,pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/cuvolene.png'
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(230, 790, u"LISTADO DE BATERIAS")
        
    def tabla(self,pdf,y):
        encabezados = ('Descripcion')
        detalles = [(baterias.descripcion) for baterias in Baterias.objects.all().order_by('descripcion')]
        detalle_orden = Table([encabezados] + detalles, colWidths=[16 * cm])
        detalle_orden.setStyle(TableStyle(
            [
                ('ALIGN',(0,0),(0,0),'CENTER'),
                ('GRID', (0, 0), (0, 0), 1, colors.black), 
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60,y)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 670
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

class ReporteCauchosPDF(View):  
     
    def cabecera(self,pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/cuvolene.png'
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(230, 790, u"LISTADO DE CAUCHOS")
        
    def tabla(self,pdf,y):
        encabezados = ('Descripcion')
        detalles = [(cauchos.descripcion) for cauchos in Cauchos.objects.all().order_by('descripcion')]
        detalle_orden = Table([encabezados] + detalles, colWidths=[16 * cm])
        detalle_orden.setStyle(TableStyle(
            [
                ('ALIGN',(0,0),(0,0),'CENTER'),
                ('GRID', (0, 0), (0, 0), 1, colors.black), 
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60,y)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 670
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

class ReporteRinesPDF(View):  


     
    def cabecera(self,pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/cuvolene.png'
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(230, 790, u"LISTADO DE RINES")
        
    def tabla(self,pdf,y):
        encabezados = ('Descripcion')
        detalles = [(rines.descripcion) for rines in Rines.objects.all().order_by('descripcion')]
        detalle_orden = Table([encabezados] + detalles, colWidths=[16 * cm])
        detalle_orden.setStyle(TableStyle(
            [
                ('ALIGN',(0,0),(0,0),'CENTER'),
                ('GRID', (0, 0), (0, 0), 1, colors.black), 
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        detalle_orden.wrapOn(pdf, 800, 600)
        detalle_orden.drawOn(pdf, 60,y)

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer)
        self.cabecera(pdf)
        y = 670
        self.tabla(pdf, y)
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

class ReporteAceitesPDF(View):  
     
    def cabecera(self,pdf):
        archivo_imagen = settings.STATIC_ROOT+'/images/cuvolene.png'
        pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)
        
        pdf.setFont("Helvetica", 16)
        pdf.drawString(230, 790, u"LISTADO DE ACEITES")
        
    def tabla(self,pdf,y):
        encabezados = ('Tipo', 'Descripcion')
        detalles = [(aceites.tipo, aceites.descripcion) for aceites in Aceites.objects.all().order_by('tipo')]
        detalle_orden = Table([encabezados] + detalles, colWidths=[8 * cm, 8 * cm])
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(1,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (1, 0), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60,y)

    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        y = 670
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response