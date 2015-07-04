from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView
from .models import Post


@login_required
def index(request):
    return render_to_response(
        'posting/index.html',
        RequestContext(
            request,
            {}
        )
    )


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        return super(PostDetailView, self).get_context_data(**kwargs)
