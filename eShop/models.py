from django.db import models


# Create your models here.
class Produse(models.Model):
    Firma = models.CharField(max_length=45, blank=True, null=True, default=None)
    Data_expirare = models.DateField(null=True, blank=True, default=None)
    Data_fabricatie = models.DateField(null=True, blank=True, default=None)

    def __str__(self):
        return f"{self.Firma}"


class Comenzi(models.Model):
    Oras = models.CharField(max_length=45, blank=True, null=True, default=None)
    Strada = models.CharField(max_length=45, blank=True, null=True, default=None)
    Nume_Client = models.CharField(max_length=45, blank=True, null=True, default=None)

    def __str__(self):
        return f"{self.Nume_Client}"


class Magazine(models.Model):
    Oras = models.CharField(max_length=45, blank=True, null=True, default=None)
    Strada = models.CharField(max_length=45, blank=True, null=True, default=None)
    produs = models.ForeignKey(Produse, on_delete=models.CASCADE)
    comanda = models.ForeignKey(Comenzi, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Strada} {self.Oras}"
