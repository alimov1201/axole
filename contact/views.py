from django.shortcuts import render
from contact.forms import ContactForm
from contact.models import Contact


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    field = Contact.objects.all()
    context = {
        'contact': field,
        'form': form
    }
    return render(request=request, template_name='contact.html', context=context)
