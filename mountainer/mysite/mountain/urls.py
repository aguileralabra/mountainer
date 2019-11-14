from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('FormularioTurist',views.crearTurist,name='FormularioTurist'),
    path('hecho',views.hecho,name='hecho'),
    path('editar',views.editarTurist,name='editar'),
    path('galeria', views.galeria, name='galeria'),
    path('contacto', views.contacto, name='contacto'),
    path('turists/', views.TuristListView.as_view(), name='turists'),
    path('turists/<int:pk>', views.TuristDetailView.as_view(), name='turist-detail'),
]
