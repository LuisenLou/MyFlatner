from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),    
    path('auth/', include ('djoser.social.urls')),
    path('admin/', admin.site.urls),

    path('api/flat/', include('apps.flat.urls')),
    path('api/room/', include('apps.room.urls')),
    path('api/address/', include('apps.address.urls')),
    path('api/incident/', include('apps.incident.urls')),
    path('api/task/', include('apps.task.urls')),
    path('api/contact/', include('apps.contact_form.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*',TemplateView.as_view(template_name='index.html'))]
