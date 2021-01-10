from django.shortcuts import render
from .models import post
from comments.forms import CommentForm

def ProductList(request):
    queryset = post.objects.all()
    context = {
        'my_list': queryset
    }
    return render(request, 'article_list.html', context)


def ArticleDetail(request,my_id):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CommentForm()

    obj = post.objects.get(id=my_id)
    context = {
        "item": obj,
        'form': form
    }
    return render(request, 'article.html', context)
