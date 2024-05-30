from django.shortcuts import render
from contact.forms import ContactForm

def create(request):
    if request.method == 'POST':
        ctx = {'form': ContactForm(request.POST)}

        return render(request, 'contact/create.html', ctx)

    ctx = {'form': ContactForm()}

    return render(request, 'contact/create.html', ctx)