from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from principal import views

from django.contrib import admin

urlpatterns = [
    url(r'^principal/$',login_required(views.principal.as_view()), name='principal'),  

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

    # Socio 
    url(r'^socios/$',login_required(views.principal_socios.as_view()), name='principal_socios'),
    url(r'^socios/agregar/$',login_required(views.principal_agregar_socio.as_view()), name='socio_create'),    
    url(r'^socios/editar/(?P<pk>\d+)$',login_required(views.principal_editar_socio.as_view()), name='socio_edit'),
    url(r'^socios/eliminar/(?P<pk>\d+)$',login_required(views.principal_eliminar_socio.as_view()), name='socio_delete'),
    
    url(r'^reporte_personas_pdf/$',login_required(views.ReportePersonasPDF.as_view()), name="reporte_personas_pdf"),     
    url(r"^principal_cooperativas/$", TemplateView.as_view(template_name="principal_cooperativas.html"), name="principal_cooperativas"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
