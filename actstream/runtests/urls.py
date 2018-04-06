import os
from django.contrib import admin, auth
from django.views.static import serve
try:
    from django.urls import include, url
except ImportError:
    from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': os.path.join(os.path.dirname(__file__), 'media')}),
    url(r'auth/', include('auth.urls')),
    url(r'testapp/', include('testapp.urls')),
    url(r'', include('actstream.urls')),
]
