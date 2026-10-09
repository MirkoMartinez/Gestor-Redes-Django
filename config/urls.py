from django.contrib import admin
from django.urls import path, include
from gestor import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea activa el sistema de login de Django
    path('cuentas/', include('django.contrib.auth.urls')), 
    
    path('', views.lista_clientes, name='inicio'),
    path('cliente/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('post/<int:post_id>/editar/', views.editar_publicacion, name='editar_publicacion'),
    path('post/<int:post_id>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)