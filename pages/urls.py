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
]