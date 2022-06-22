from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('news/', include('news.urls')),
    path('contact/', include('contact.urls')),
    path('spna_admin/', include('spna_admin.urls')),
    path('member/', include('member.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'spna.views.page_not_found'
handler500 = 'spna.views.server_not_found'