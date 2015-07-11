from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from authenticating.views import complete_invitation
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Builtin urls
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include('django_markdown.urls')),

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
