from django.conf.urls import include, url
from django.contrib import admin
from authenticating.views import complete_invitation


urlpatterns = [
    # Builtin urls
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Invitation response
    url(
        r'^accounts/invitation/(?P<pk>[^/]+)/$',
        complete_invitation,
    ),

    # Current home app
    url(r'^', include('posting.urls'))
]
