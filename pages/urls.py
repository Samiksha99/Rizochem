from django.urls import path
from . import views

urlpatterns = [
    path('allopathic',views.allopathic, name='allopathic'),
    path('ayurvedic',views.ayurvedic, name='ayurvedic'),
    path('disposals',views.disposals, name='disposals'),
    path('neu',views.neu, name='neu'),
    path('pharmacy',views.pharmacy, name='pharmacy'),
    path('resp',views.resp, name='resp'),
    path('surgicals',views.surgicals, name='surgicals'),
    path('orth',views.orth, name='orth'),
    path('app',views.app, name='app'),
    path('belt',views.belt, name='belt'),
    path('cerv',views.cerv, name='cerv'),
    path('fing',views.fing, name='fing'),
    path('frac',views.frac, name='frac'),
    path('gel',views.gel, name='gel'),
    path('knee',views.knee, name='knee'),
    path('neo',views.neo, name='neo'),
    path('trac',views.trac, name='trac'),
    path('wri',views.wri, name='wri'),
    path('diag',views.diag, name='diag'),
    path('cath',views.cath, name='cath'),
    path('fluid',views.fluid, name='fluid'),
    
    
]