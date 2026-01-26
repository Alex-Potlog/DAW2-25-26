
from django.http import HttpResponse
from django.views.generic import ListView

from blog.models import Article

# Create your views here.


def hola_món(request):
    return HttpResponse("Hola món!")


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
