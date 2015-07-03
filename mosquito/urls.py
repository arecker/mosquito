from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Builtin urls
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Current home app
    url(r'^', include('posting.urls'))
]
