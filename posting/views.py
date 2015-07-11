from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from .models import Post
from .forms import TextPostForm, LinkPostForm, ImagePostForm


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


@login_required
def add(request, slug):
    form_class = {
        'text': TextPostForm,
        'link': LinkPostForm,
        'image': ImagePostForm
    }.get(slug, None)

    if not form_class:
        raise Http404

    if request.method == 'POST':
        form = form_class(request.POST)
    else:
        form = form_class()

    return render_to_response(
        'posting/add.html',
        RequestContext(request, {'form': form})
    )
