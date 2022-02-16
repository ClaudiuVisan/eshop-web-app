from django.shortcuts import render, redirect, get_object_or_404
from eShop.forms import *
from django.contrib import messages


# Create your afisares here.
def index(request):
    return render(request, 'index.html')


def afisare_produse(request):
    listaproduse = Produse.objects.order_by('Data_fabricatie')
    produsedict = {'produse': listaproduse}
    return render(request, 'produse.html', context=produsedict)


def afisare_comenzi(request):
    listacomenzi = Comenzi.objects.order_by('Nume_Client')
    comenzidict = {'comenzi': listacomenzi}
    return render(request, 'comenzi.html',
                  context=comenzidict)


def afisare_magazine(request):
    listamagazine = Magazine.objects.order_by('Oras')
    magazinedict = {'magazine': listamagazine}
    return render(request, 'magazine.html', context=magazinedict)


def adaugare_produs(request):
    if request.method == 'POST':
        produs_form = ProdusForm(request.POST)
        if produs_form.is_valid():
            produs_form.save()
            messages.success(request, 'Produs adaugat')
        else:
            messages.error(request, 'Eroare salvare')

        return redirect('/produse')

    produs_form = ProdusForm()
    produse = Produse.objects.all()
    return render(request, 'adaugareProdus.html',
                  context={'produs_form': produs_form,
                           'produs': produse})


def adaugare_comanda(request):
    if request.method == 'POST':
        comanda_form = ComandaForm(request.POST)
        if comanda_form.is_valid():
            comanda_form.save()
            messages.success(request, 'Comanda adaugata')
        else:
            messages.error(request, 'Eroare salvare')

        return redirect("/comenzi")
    comanda_form = ComandaForm()
    return render(request, 'adaugareComanda.html',
                  context={'comanda_form': comanda_form})


def adaugare_magazin(request):
    if request.method == 'POST':
        magazin_form = MagazinForm(request.POST)
        if magazin_form.is_valid():
            magazin_form.save()
            messages.success(request, 'Magazin adaugat')
        else:
            messages.error(request, 'Eroare salvare')
        return redirect('/magazine')
    magazin_form = MagazinForm()
    return render(request, 'adaugareMagazin.html',
                  context={'magazin_form': magazin_form})


def editare_produs(request, id):
    produs = get_object_or_404(Produse, id=id)
    if request.method == 'POST':
        editare_form = ProdusForm(request.POST, instance=produs)
        if editare_form.is_valid():
            editare_form.save()
            return redirect('/produse')
    else:
        editare_form = ProdusForm(instance=produs)

    editare_form = ProdusForm()
    return render(request, 'editareProdus.html',
                  {
                      'form': editare_form,
                      'produs': produs,
                  })


def editare_comanda(request, id):
    comanda = get_object_or_404(Comenzi, id=id)
    if request.method == 'POST':
        editare_form = ComandaForm(request.POST, instance=comanda)
        if editare_form.is_valid():
            editare_form.save()
            return redirect('/comenzi')
    else:
        editare_form = ComandaForm(instance=comanda)

    editare_form = ComandaForm()
    return render(request, 'editareComanda.html',
                  {
                      'form': editare_form,
                      'comanda': comanda,
                  })


def editare_magazin(request,id):
    magazin = get_object_or_404(Magazine, id=id)
    if request.method == 'POST':
        editare_form = MagazinForm(request.POST, instance=magazin)
        if editare_form.is_valid():
            editare_form.save()
            return redirect('/magazine')
    else:
        editare_form = MagazinForm(instance=magazin)

    editare_form = MagazinForm()
    return render(request, 'editareMagazin.html',
                  {
                      'form': editare_form,
                      'magazin': magazin,
                  })


def stergere_produs(request, id):
    produs = get_object_or_404(Produse, id=id)
    if request.method == 'POST':
        stergere_form = ProdusDeleteForm(request.POST, instance=produs)
        if stergere_form.is_valid():
            produs.delete()
            return redirect('/produse')
    else:
        stergere_form = ProdusDeleteForm(instance=produs)

    stergere_form = ProdusDeleteForm()
    return render(request, 'produse.html',
                  {
                      'form': stergere_form,
                      'produs': produs,
                  })


def stergere_comanda(request, id):
    comanda = get_object_or_404(Comenzi, id=id)
    if request.method == 'POST':
        stergere_form = ComandaDeleteForm(request.POST, instance=comanda)
        if stergere_form.is_valid():
            comanda.delete()
            return redirect('/comenzi')
    else:
        stergere_form = ComandaDeleteForm(instance=comanda)

    stergere_form = ComandaDeleteForm()
    return render(request, 'comenzi.html',
                  {
                      'form': stergere_form,
                      'comanda': comanda,
                  })


def stergere_magazin(request, id):
    magazin = get_object_or_404(Magazine, id=id)
    if request.method == 'POST':
        stergere_form = MagazinDeleteForm(request.POST, instance=magazin)
        if stergere_form.is_valid():
            magazin.delete()
            return redirect('/magazine')
    else:
        delete_form = MagazinDeleteForm(instance=magazin)

    stergere_form = MagazinDeleteForm()
    return render(request, 'magazine.html',
                  {
                      'form': stergere_form,
                      'magazin': magazin,
                  })

