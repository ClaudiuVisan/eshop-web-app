from django.urls import path
from eShop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('magazine/', views.afisare_magazine, name='magazine'),
    path('comenzi/', views.afisare_comenzi, name='comenzi'),
    path('produse/', views.afisare_produse, name='produse'),
    path('magazine/adaugare-magazin', views.adaugare_magazin,
         name='adaugare_magazin'),
    path('comenzi/adaugare-comanda', views.adaugare_comanda,
         name='adaugare_comanda'),
    path('produse/adaugare-produs', views.adaugare_produs,
         name='adaugare_produs'),
    path('magazine/editare-magazin/<int:id>', views.editare_magazin,
         name='editare_magazin'),
    path('produse/editare-produs/<int:id>', views.editare_produs,
         name='editare_produs'),
    path('comenzi/editare-comanda/<int:id>', views.editare_comanda,
         name='editare_comanda'),
    path('magazine/stergere-magazin/<int:id>', views.stergere_magazin,
         name='stergere_magazin'),
    path('produse/stergere-produs/<int:id>', views.stergere_produs,
         name='stergere_produs'),
    path('comenzi/stergere-comanda/<int:id>', views.stergere_comanda,
         name='stergere_comanda'),
]
