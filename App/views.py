from django.shortcuts import render, redirect
import requests
from .models import Country
from .forms import CountryForm


# def index(request):
#     url = 'https://coronavirus-tracker-api.herokuapp.com/v2/locations?country={}'
#     countries = Country.objects.all()

#     if request.method == 'POST':
#         form = CountryForm(request.POST)
#         form.save()
#         return redirect('/')
#     else:
#         form = CountryForm()
#     corona_data = []
#     for country in countries:
#         r = requests.get(url.format(country)).json()
#         print(r)
#         country_update = {

#         }

#         corona_data.append(country_update)
#     context = {
#         'corona_data': corona_data,
#         'form': form,
#         'countries': countries,
#     }
#     return render(request, 'index.html', context)


def index(request):
    url = 'https://coronavirus-tracker-api.herokuapp.com/v2/locations?country={}'
    countries = Country.objects.all()

    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            new_country = form.cleaned_data['country_name']
            existing_country_count = Country.objects.filter(
                country_name=new_country).count()

            if existing_country_count == 0:
                r = requests.get(url.format(new_country)).json()
                print(r)
                form.save()
            else:
                print('Country Already exists')
    else:
        form = CountryForm()

    main_data = []
    for country in countries:
        r = requests.get(url.format(country)).json()
        print(r)
        corona_data = {
            'country': country.country_name,
            'deaths': r['latest']['deaths'],
            'recovered': r['latest']['recovered'],
            'cases': r['latest']['confirmed'],
        }
        main_data.append(corona_data)

    context = {
        'main_data': main_data,
        'counties': countries,
        'form': form,
    }

    return render(request, 'index.html', context)


def delete(request, name):
    Country.objects.get(country_name=name).delete()
    return redirect('/')
