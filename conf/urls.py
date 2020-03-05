from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apps.general.views import home_page

admin.autodiscover()
admin.site.site_header = 'Панель управления'
urlpatterns = [
    path('admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', home_page, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
