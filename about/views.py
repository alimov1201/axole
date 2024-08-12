from django.shortcuts import render
from blog.forms import EmailForm


def about(request):
    form = EmailForm()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }

    return render(request, 'about.html', context=context)
