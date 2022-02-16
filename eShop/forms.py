from django.forms import ModelForm
from eShop.models import *


class ProdusForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProdusForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Produse
        fields = '__all__'


class ProdusDeleteForm(ModelForm):
    class Meta:
        model = Produse
        fields = []


class ComandaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComandaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Comenzi
        fields = '__all__'


class ComandaDeleteForm(ModelForm):
    class Meta:
        model = Comenzi
        fields = []

        
class MagazinForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(MagazinForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Magazine
        fields = '__all__'


class MagazinDeleteForm(ModelForm):
    class Meta:
        model = Magazine
        fields = []
