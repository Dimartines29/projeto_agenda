from django.shortcuts import render
from contact.models import Contact


def index(request):
    contacts = Contact.objects.all()

    ctx = {'contacts': contacts,}

    return render(request, 'contact/index.html', ctx)

