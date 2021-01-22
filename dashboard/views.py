import csv
from django.shortcuts import render


# Create your views here.
def listHosp(request):
    datas = csv.DictReader(open(r"./files/donnees-hospitalieres-classe-age-covid19-2021-01-20-19h03.csv", "r"),delimiter=';')
    out = [row for row in datas]
    return render(request, 'dashboard/index.html', {'datas': out})


def afficheDash(request):
    return render(request, 'dashboard/affichedash.html')

def afficheDashMoy(request):
    return render(request, 'dashboard/affichedashmoy.html' )