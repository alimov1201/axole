from django.shortcuts import render, get_object_or_404
from blog.models import Article
from blog.forms import EmailForm

def blog(request):
    form = EmailForm()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()

    articles = Article.objects.all()
    context = {
        "articles": articles,
        'form': form,
    }

    return render(request=request, template_name='index.html', context=context)


def detail(request, pk):
    form = EmailForm()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
    article = get_object_or_404(Article, pk=pk)
    context = {
        "article": article,
        'form': form
    }
    return render(request, 'blog-single.html', context)
