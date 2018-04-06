import os
from django.contrib import admin, auth
from django.views.static import serve
from actstream import urls as actstream_urls
from testapp import urls as testapp_urls
try:
    from django.urls import include, url
except ImportError:
    from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls)),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': os.path.join(os.path.dirname(__file__), 'media')}),
    url(r'auth/', auth.urls),
    url(r'testapp/', testapp_urls),
    url(r'', actstream_urls),
]
