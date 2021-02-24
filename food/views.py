from django.shortcuts import render
from .models import BurgerKing
from .get_distances import count_distance


def home(request):
    bks = BurgerKing.objects.all()
    comp_count = 0
    competitors = []
    if request.method == "POST":
        adrs = request.POST.get('address')
        competitors += count_distance('food_mcdonalds', adrs)
        competitors += count_distance('food_kfc', adrs)
        comp_count = len(competitors)
#   get address and restaurant's name
    companies = [(i[0][4], i[0][1]) for i in competitors]
    return render(request, 'home.html', {'bks': bks, 'comp_count': comp_count, 'companies': companies})
