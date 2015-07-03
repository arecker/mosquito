from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Account, Invitation


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Site Account'


class InvitationInline(admin.StackedInline):
    model = Invitation
    extra = 0


class UserAdmin(UserAdmin):
    inlines = (AccountInline, InvitationInline)


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
