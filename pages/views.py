from django.shortcuts import render
from . models import allos
from . models import ayurs
from . models import disps
from . models import neuts
from . models import pharms
from . models import respis
from . models import surgis
# Create your views here.


def allopathic(request):
    allo = allos.objects.all()

    return render(request, "allopathic.html", {'allo': allo})

def ayurvedic(request):
    ayur = ayurs.objects.all()

    return render(request, "ayurvedic.html", {'ayur': ayur})

def disposals(request):
    disp = disps.objects.all()

    return render(request, "disposals.html", {'disp': disp})

def neu(request):
    neut = neuts.objects.all()

    return render(request, "neu.html", {'neut': neut})

def pharmacy(request):
    pharm = pharms.objects.all()

    return render(request, "pharmacy.html", {'pharm': pharm})

def resp(request):
    respi = respis.objects.all()

    return render(request, "resp.html", {'respi': respi})

def surgicals(request):
    surgi = surgis.objects.all()

    return render(request, "surgicals.html", {'surgi': surgi})
