from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from principal.forms import OrderedItemForm

from principal import views

from django.contrib import admin

urlpatterns = [
    url(r'^principal/$',login_required(views.principal.as_view()), name='principal'),  

    url(r'^recetas/lista/$', 'principal.views.vehiculos', name='lista'),
    url(r'^recetas/registrar/$', 'principal.views.registro_edicion', name='registrar'),
    url(r'^recetas/(?P<vehiculo_id>\d+)/$', 'principal.views.registro_edicion', name='editar'), 

    # Cooperativa 
    url(r'^cooperativas/$',login_required(views.principal_cooperativas.as_view()), name='principal_coop'),
    url(r'^cooperativas/agregar/$',login_required(views.principal_agregar_cooperativa.as_view()), name='cooperativa_create'),    
    url(r'^cooperativas/editar/(?P<pk>\d+)$',login_required(views.principal_editar_cooperativa.as_view()), name='cooperativa_edit'),
    url(r'^cooperativas/eliminar/(?P<pk>\d+)$',login_required(views.principal_eliminar_cooperativa.as_view()), name='cooperativa_delete'),
    url(r'^reporte_cooperativas_pdf/$',login_required(views.ReporteCooperativasPDF.as_view()), name="reporte_cooperativas_pdf"), 

    # Socio 
    url(r'^socios/$',login_required(views.principal_socios.as_view()), name='principal_socios'),
    url(r'^socios/agregar/$',login_required(views.principal_agregar_socio.as_view()), name='socio_create'),    
    url(r'^socios/editar/(?P<pk>\d+)$',login_required(views.principal_editar_socio.as_view()), name='socio_edit'),
    url(r'^socios/eliminar/(?P<pk>\d+)$',login_required(views.principal_eliminar_socio.as_view()), name='socio_delete'),
    url(r'^reporte_socios_pdf/$',login_required(views.ReporteSociosPDF.as_view()), name="reporte_socios_pdf"),               

    # Vehiculo 
    url(r'^vehiculos/$',login_required(views.principal_vehiculos.as_view()), name='principal_vehiculos'),
    url(r'^vehiculos/agregar/$',login_required(views.principal_agregar_vehiculo.as_view()), name='vehiculo_create'),    
    #url(r'^vehiculos/editar/(?P<pk>\d+)$',login_required(views.principal_editar_vehiculo2.as_view()), name='vehiculo_edit2'),
    url(r'^vehiculos/eliminar/(?P<pk>\d+)$',login_required(views.principal_eliminar_vehiculo.as_view()), name='vehiculo_delete'),
    url(r'^reporte_vehiculos_pdf/$',login_required(views.ReporteVehiculosPDF.as_view()), name="reporte_vehiculos_pdf"),  
    #url(r'^inline-formset/$', views.editar_vehiculo,
    #   {'form_class': OrderedItemForm, 'template': 'inline-formset.html'}, name='vehiculo_edit1'),     
    #url(r'^vehiculos/editar/(?P<pk>\d+)$',login_required(views.principal_editar_vehiculo.as_view()), name='vehiculo_edit'),       
    #url(r'^vehiculos/editar/(?P<pk>\d+)$', views.editar_vehiculo,
    #   {'form_class': OrderedItemForm, 'template': 'principal_vehiculos_detalle.html'}, name='vehiculo_edit'),     
    url(r'^vehiculos/editar/(?P<pk>\d+)$',login_required(views.principal_vehiculos_bateria.as_view()), name='vehiculo_edit'),

    #Marca
    url(r'^marcas/$',login_required(views.principal_marcas.as_view()), name='principal_marcas'),
    url(r'^marcas/agregar/$',login_required(views.principal_agregar_marca.as_view()), name='marca_create'),    
    url(r'^marcas/editar/(?P<pk>\d+)$',login_required(views.principal_editar_marca.as_view()), name='marca_edit'),
    url(r'^marcas/eliminar/(?P<pk>\d+)$',login_required(views.principal_eliminar_marca.as_view()), name='marca_delete'),
    url(r'^reporte_marcas_pdf/$',login_required(views.ReporteMarcasPDF.as_view()), name="reporte_marcas_pdf"),    

    #Bateria
    url(r'^baterias/$',login_required(views.principal_baterias.as_view()), name='principal_baterias'),
    url(r'^baterias/agregar/$',login_required(views.principal_agregar_bateria.as_view()), name='bateria_create'),    
    url(r'^baterias/editar/(?P<pk>\d+)$',login_required(views.principal_editar_bateria.as_view()), name='bateria_edit'),
    url(r'^baterias/eliminar/(?P<pk>\d+)$',login_required(views.principal_eliminar_bateria.as_view()), name='bateria_delete'),
    url(r'^reporte_baterias_pdf/$',login_required(views.ReporteBateriasPDF.as_view()), name="reporte_baterias_pdf"),    

    #Caucho
    url(r'^cauchos/$',login_required(views.principal_cauchos.as_view()), name='principal_cauchos'),
    url(r'^cauchos/agregar/$',login_required(views.principal_agregar_caucho.as_view()), name='caucho_create'),    
    url(r'^cauchos/editar/(?P<pk>\d+)$',login_required(views.principal_editar_caucho.as_view()), name='caucho_edit'),
    url(r'^cauchos/eliminar/(?P<pk>\d+)$',login_required(views.principal_eliminar_caucho.as_view()), name='caucho_delete'),
    url(r'^reporte_cauchos_pdf/$',login_required(views.ReporteCauchosPDF.as_view()), name="reporte_cauchos_pdf"), 
   
   #Rin
    url(r'^rines/$',login_required(views.principal_rines.as_view()), name='principal_rines'),
    url(r'^rines/agregar/$',login_required(views.principal_agregar_rin.as_view()), name='rin_create'),    
    url(r'^rines/editar/(?P<pk>\d+)$',login_required(views.principal_editar_rin.as_view()), name='rin_edit'),
    url(r'^rines/eliminar/(?P<pk>\d+)$',login_required(views.principal_eliminar_rin.as_view()), name='rin_delete'),
    url(r'^reporte_rines_pdf/$',login_required(views.ReporteRinesPDF.as_view()), name="reporte_rines_pdf"), 


    #Aceite
    url(r'^aceites/$',login_required(views.principal_aceites.as_view()), name='principal_aceites'),
    url(r'^aceites/agregar/$',login_required(views.principal_agregar_aceite.as_view()), name='aceite_create'),    
    url(r'^aceites/editar/(?P<pk>\d+)$',login_required(views.principal_editar_aceite.as_view()), name='aceite_edit'),
    url(r'^aceites/eliminar/(?P<pk>\d+)$',login_required(views.principal_eliminar_aceite.as_view()), name='aceite_delete'),
    url(r'^reporte_aceites_pdf/$',login_required(views.ReporteAceitesPDF.as_view()), name="reporte_aceites_pdf"),    
    
  #Filtro
    url(r'^filtros/$',login_required(views.principal_filtros.as_view()), name='principal_filtros'),
    url(r'^filtros/agregar/$',login_required(views.principal_agregar_filtro.as_view()), name='filtro_create'),    
    url(r'^filtros/editar/(?P<pk>\d+)$',login_required(views.principal_editar_filtro.as_view()), name='filtro_edit'),
    url(r'^filtros/eliminar/(?P<pk>\d+)$',login_required(views.principal_eliminar_filtro.as_view()), name='filtro_delete'),
    url(r'^reporte_filtros_pdf/$',login_required(views.ReporteFiltrosPDF.as_view()), name="reporte_filtros_pdf"),        
   
    url(r"^principal_cooperativas/$", TemplateView.as_view(template_name="principal_cooperativas.html"), name="principal_cooperativas"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
