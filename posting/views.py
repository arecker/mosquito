from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from .models import Post


@login_required
def index(request):
    return render_to_response(
        'posting/index.html',
        RequestContext(
            request,
            {
                'posts': Post.objects.all()
            }
        )
    )


@login_required
def post_detail(request, pk):
    return render_to_response(
        'posting/post_detail.html',
        RequestContext(
            request,
            {
                'post': get_object_or_404(Post, pk=pk)
            }
        )
    )
