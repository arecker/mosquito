from django.contrib import admin
from .models import TextPost, ImagePost, LinkPost


admin.site.register(TextPost)
admin.site.register(ImagePost)
admin.site.register(LinkPost)
