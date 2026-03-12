"""
URL configuration for gestion_etiquetas_qr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from modulo_gestion_qr import views
from modulo_gestion_qr.forms import CustomLoginForm


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html', 
        authentication_form=CustomLoginForm
    ), name='login'),  # Vista personalizada para login
    path('logout/', views.custom_logout, name='logout'),  # Vista de logout personalizada
    path('', views.generar_seriales, name='home'),  # Redirige raíz a asociar_seriales
    #path('seriales', views.ver_seriales, name='ver_seriales'),
    path('asociar/', views.generar_seriales, name='generar_seriales'),
    path('success/', views.serial_success, name='serial_success'),
    path('<str:cliente_slug>/qr/', views.ver_informacion_qr, name='ver_informacion_qr'),
    path('cliente/nuevo/', views.ClienteCreateView.as_view(), name='crear_cliente'),
    path('cliente/exito/<int:pk>/', views.ClienteSuccessView.as_view(), name='cliente_success'),
    path('producto/nuevo/', views.ProductoCreateView.as_view(), name='crear_producto'),
    path('producto/exito/<int:pk>/', views.ProductoSuccessView.as_view(), name='producto_success'),
    path('index/', views.index, name='index'),  # Define la vista principal
    #path('actualizar_seriales/', views.actualizar_seriales, name='actualizar_seriales'),
    path('api/productos/<int:cliente_id>/', views.productos_por_cliente, name='productos_por_cliente'),
    path('actualizar/', views.asociar_seriales, name='asociar_seriales'),
    path('actualizar-exito/', views.asociar_seriales, name='asociar_exito'),
    path('buscar/', views.buscar_seriales, name='buscar_seriales'),
    path('cargar-productos/<int:cliente_id>/', views.productos_por_cliente, name='cargar_productos'),
    path('clientes/', views.listado_clientes, name='listado_clientes'),
    path('productos/', views.listado_productos, name='listado_productos'),
    path('crear-template/', views.crear_template_cliente, name='crear_template_cliente'),
    path('listado-templates/', views.listado_templates, name='listado_templates'),  
    path('api/obtener_campos_seriales/', views.obtener_campos_seriales, name='obtener_campos_seriales'),
    path('producto/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('api/templates/<int:cliente_id>/', views.obtener_templates_por_cliente, name='obtener_templates_por_cliente'),
    path('exportar_csv/', views.exportar_csv, name='exportar_csv'),
    path('solicitud/nueva/', views.crear_solicitud, name='crear_solicitud'),
    path('landing/<str:codigo>/', views.landing_solicitud, name='landing_solicitud'),
    path('solicitud/<int:solicitud_id>/editar/', views.editar_solicitud, name='editar_solicitud'),
    path('solicitud/buscar/', views.buscar_solicitud, name='buscar_solicitud'),
    path('solicitud/ver/<int:solicitud_id>/', views.ver_solicitud, name='ver_solicitud'),
    path('cinta/<str:serial>/', views.landing_serial_qr, name='landing_serial_qr'),
    path('entrega/', views.formulario_entrega, name='formulario_entrega'),
    path('api/solicitud_por_rango/', views.solicitud_por_rango, name='solicitud_por_rango'),
    path("buscar-nit/", views.buscar_nit, name="buscar_nit"),
    path('asignar-serial-interno/', views.asignar_seriales_interno, name='asignar_serial_interno'),
    path('serial-interno/<str:serial_interno>/', views.landing_serial_interno, name='landing_serial_interno'),
    path('seriales/por-producto/<int:producto_id>/', views.seriales_por_producto, name='seriales_por_producto'),
    path('seriales/asignados-a/<int:serial_id>/', views.seriales_asignados_a, name='seriales_asignados_a'),
    path('asociar/por-serial-interno/', views.asociar_por_serial_interno, name='asociar_por_serial_interno'),
    path('exportar-seriales/', views.exportar_csv, name='exportar_csv'),
    path('exportar_csv_personalizado/', views.exportar_csv_personalizado, name='exportar_csv_personalizado'),
    path("generar-acta/", views.generar_acta, name="generar_acta"),
   
    path('<slug:cliente_slug>/', views.crear_template_cliente, name='template_cliente'),


]

#if settings.DEBUG and not settings.USE_S3:
 #   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:   
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







