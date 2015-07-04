from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from authenticating.views import complete_invitation

"""
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^about/', TemplateView.as_view(template_name="about.html")),
]
"""


urlpatterns = [
    # Builtin urls
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Invitation response
    url(
        r'^accounts/invitation/complete/$',
        TemplateView.as_view(
            template_name="registration/invitation_instructions.html"
        ),
        name="invitation_instructions"
    ),
    url(
        r'^accounts/invitation/(?P<pk>[^/]+)/$',
        complete_invitation,
    ),

    # Current home app
    url(r'^', include('posting.urls'))
]
