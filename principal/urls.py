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

    # Socio 
    url(r'^socios/$',login_required(views.principal_socios.as_view()), name='principal_socios'),
    url(r'^socios/agregar/$',login_required(views.principal_agregar_socio.as_view()), name='socio_create'),    
    url(r'^socios/editar/(?P<pk>\d+)$',login_required(views.principal_editar_socio.as_view()), name='socio_edit'),
    url(r'^socios/eliminar/(?P<pk>\d+)$',login_required(views.principal_eliminar_socio.as_view()), name='socio_delete'),
    
    url(r'^reporte_personas_pdf/$',login_required(views.ReportePersonasPDF.as_view()), name="reporte_personas_pdf"),     
    url(r"^principal_cooperativas/$", TemplateView.as_view(template_name="principal_cooperativas.html"), name="principal_cooperativas"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
