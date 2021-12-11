from django.shortcuts import render, redirect, HttpResponse
from phones.models import Phone
import re


def index(request):
    # phone_objects = Phone.objects.all()
    # phone = [f'{c.id}: {c.name}, {c.price}: {c.image} | {c.slug}' for c in phone_objects]
    # return HttpResponse('<br>'.join(phone))

    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', '-name')
    print(sort)
    phone_objects = Phone.objects.all()
    context = {'phones': phone_objects.extra(order_by = [sort])}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug=slug)
    context = {'phone': phone_objects.values()[0]}
    return render(request, template, context)
