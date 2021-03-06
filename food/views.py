from django.shortcuts import render
from .models import BurgerKing
from .get_distances import count_distance
from .forms import Form

def home(request):
    bks = BurgerKing.objects.all()
    comp_count = 0
    competitors = []
    adrs = ''
#   get data from form
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            adrs = form.cleaned_data['address']
#   choose competitors in less than 2 km with func count_distance from get_distances.py
            competitors += count_distance('food_mcdonalds', adrs)
            competitors += count_distance('food_kfc', adrs)
            comp_count = len(competitors)
    else:
        form = Form()
#   get address and restaurant's name
    companies = [(i[0][4], i[0][1]) for i in competitors]
    return render(request, 'home.html', {'bks': bks, 'comp_count': comp_count,
                                         'companies': companies, 'form': form, 'adrs': adrs})
