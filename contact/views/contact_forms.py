from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact

def create(request):
    ctx = {}

    return render(request, 'contact/create.html', ctx)