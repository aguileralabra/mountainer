from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
	path('', include('mountain.urls')),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

admin.site.site_header = "Administracion de Mountain Break"
admin.site.index_title = "Mountain Break ADMINISTRACION"

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
