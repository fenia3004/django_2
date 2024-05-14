from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from catalog.models import Product, Blog


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


def base(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/product_list.html", context)


def contacts(request):
    """Принимает контактные данные от пользователя с сайта"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Ваше сообщение: {name}, {phone}, {message}')
        with open('write.txt', 'wt', encoding='UTF-8') as file:
            file.write(f'Ваше сообщение: {name}, {phone}, {message}')

    return render(request, 'catalog/contacts.html')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(ListView):
    model = Blog
    fields = ['title', 'text', 'image']
    success_url = reverse_lazy('catalog;:blog_list')


class BlogUpdateView(DetailView):
    model = Blog


class BlogDeleteView(DetailView):
    model = Blog


# def product_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'catalog/base.html', context)
#
#
# def product_detail(request, pk):
#     product_pk = get_object_or_404(Product, pk=pk)
#     context = {"product": product_pk}
#     return render(request, 'catalog/product_detail.html', context)


# def index(request):
#     return render(request, "catalog/home.html")
#
#
# def contacts(request):
#     return render(request, "catalog/contacts.html")
