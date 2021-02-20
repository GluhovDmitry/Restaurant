from django.shortcuts import render
from .models import Burger_king, Mcdonalds, Kfc
from .get_distances import count_distance


def home(request):
    bks = Burger_king.objects.all()
    c_len = 0
    competitors = []
    if request.method == "POST":
        adrs = request.POST.get('address')

        competitors += count_distance('food_mcdonalds', adrs)
        competitors += count_distance('food_kfc', adrs)
        for i in competitors:
            print(i)
        c_len = len(competitors)
    companies = [(i[0][4],i[0][1]) for i in competitors]
    return render(request, 'home.html', {'bks': bks, 'c_len': c_len, 'companies': companies})
