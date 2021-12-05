from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv
from pagination import settings

csv_table = []
with open(settings.BUS_STATION_CSV, newline='') as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        csv_table.append(row)

CONTENT = [str(i) for i in range(len(csv_table))]

def index(request):
    return redirect(reverse('bus_stations'))
def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    temp = csv_table[page.number-1:page.number+10]

    context = {
        'bus_stations': temp,
        'page': page}

    return render(request, 'stations/index.html', context)
