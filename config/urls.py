from django.contrib import admin
from django.urls import path
from gestor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_clientes, name='inicio'),
    path('cliente/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    
    # Nuevas rutas para edición y borrado
    path('post/<int:post_id>/editar/', views.editar_publicacion, name='editar_publicacion'),
    path('post/<int:post_id>/eliminar/', views.eliminar_publicacion, name='eliminar_publicacion'),
]