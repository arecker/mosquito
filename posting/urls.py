from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(
        r'^(?P<slug>[-\w]+)/$',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),
]
