from django.shortcuts import render, redirect

from phones.models import Phone

type_sort_phones = {
        'name': 'name',
        'max_price': '-price',
        'min_price': 'price'
    }


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    for type_sort, name_sort in type_sort_phones.items():
        if sort == type_sort:
            phones = Phone.objects.all().order_by(name_sort)
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    global context
    template = 'product.html'
    for phone in Phone.objects.all():
        if phone.slug == slug:
            context = {
                'phone': phone,
            }
    return render(request, template, context)
