from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Invitation
from .forms import AccountForm


def complete_invitation(request, pk):
    logout(request)
    invite = get_object_or_404(Invitation, pk=pk)
    if request.method == 'POST':
        form = AccountForm(
            request.POST,
            instance=invite.user.account
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = AccountForm(instance=invite.user.account)
    return render_to_response(
        'registration/complete_invitation.html',
        RequestContext(request, {
            'form': form
        })
    )
