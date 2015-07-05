from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^(?P<pk>[^/]+)/$',
        views.post_detail,
        name='post_detail'
    ),
]
