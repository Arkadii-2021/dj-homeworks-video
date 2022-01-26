from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
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
