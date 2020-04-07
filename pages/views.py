from django.shortcuts import render
from . models import allos
from . models import ayurs
from . models import disps
from . models import neuts
from . models import pharms
from . models import respis
from . models import surgis
from . models import applys
from . models import bels
from . models import cervis
from . models import fingers
from . models import fracts
from . models import gells
from . models import kneees
from . models import neops
from . models import tracts
from . models import wrists
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

def app(request):
    apply = applys.objects.all()

    return render(request, "app.html", {'apply': apply})

def belt(request):
    bel = bels.objects.all()

    return render(request, "belt.html", {'bel': bel})

def cerv(request):
    cervi = cervis.objects.all()

    return render(request, "cerv.html", {'cervi': cervi})

def fing(request):
    finger = fingers.objects.all()

    return render(request, "fing.html", {'finger': finger})

def frac(request):
    fract = fracts.objects.all()

    return render(request, "frac.html", {'fract': fract})

def gel(request):
    gell = gells.objects.all()

    return render(request, "gel.html", {'gell': gell})

def knee(request):
    kneee = kneees.objects.all()

    return render(request, "knee.html", {'kneee': kneee})

def neo(request):
    neop = neops.objects.all()

    return render(request, "neo.html", {'neops': neops})

def trac(request):
    tract = tracts.objects.all()

    return render(request, "trac.html", {'tract': tract})

def wri(request):
    wrist = wrists.objects.all()

    return render(request, "wrists.html", {'wrist': wrist})


