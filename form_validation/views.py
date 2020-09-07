import re

from django.shortcuts import render

from form_validation.data import Ticket
from form_validation.forms import TicketForm

Email_REGXF = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')

def index(request):
    errors = {}
    ticket = None
    if request.method == 'POST':
        forms = TicketForm(data=request.POST)
        is_valid = forms.is_valid()
        if is_valid:
            ticket = Ticket(
                request.POST.get('name'),
                request.POST.get('email'),
                request.POST.get('phone')
            )
            ticket.save()
    else:
        forms = TicketForm()
    context = {
        'error': errors,
        'ticket': ticket,
        'form' : forms
    }
    return render(request, 'index.html', context)

