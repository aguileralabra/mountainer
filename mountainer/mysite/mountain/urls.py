from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'), 
    path('FormularioTurist',views.crearTurist,name='FormularioTurist'),
    path('Propuestas',views.crearImagen,name='Propuestas'),
    path('resultado',views.resultado,name='resultado'),
    path('edit/<int:turist_id>', views.edit),
    path('editimagen/<int:imagen_id>', views.editimagen),
    path('delete/<int:turist_id>', views.delete),
    path('deleteimagen/<int:imagen_id>', views.deleteimagen),
    path('galeria', views.galeria, name='galeria'),
    path('login', views.login, name='login'),
    path('password_reset_form', views.password_reset_form, name='password_reset_form'),
    path('contacto', views.contacto, name='contacto'),
    path('turists/', views.TuristListView.as_view(), name='turists'),
    path('turists/<int:pk>', views.TuristDetailView.as_view(), name='turist-detail'),
    path('imagens/', views.ImagenListView.as_view(), name='imagens'),
    path('imagens/<int:pk>', views.ImagenDetailView.as_view(), name='imagen-detail'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

