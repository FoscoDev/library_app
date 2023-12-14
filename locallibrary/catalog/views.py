from django.shortcuts import render

from .models import BookInstance, Book, Author
from django.views import generic


# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status='a').count()

    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'catalog/index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #     def get_context_data(self, **kwargs):
    #         context = super(BookListView, self).get_context_data(**kwargs)
    #
    #         return context


class BookDetailView(generic.DetailView):
    model = Book

