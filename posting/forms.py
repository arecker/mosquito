from django import forms
from .models import Post


class BasePostForm(forms.ModelForm):
    def save(self, request, *args, **kwargs):
        instance = super(
            BasePostForm, self).save(commit=False)
        instance.user = request.user
        instance.save()
        return instance


class TextPostForm(BasePostForm):
    class Meta:
        model = Post
        fields = ['title', 'text']


class LinkPostForm(BasePostForm):
    class Meta:
        model = Post
        fields = ['title', 'url']


class ImagePostForm(BasePostForm):
    class Meta:
        model = Post
        fields = ['title', 'image_file']
