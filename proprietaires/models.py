from django.db import models

# Create your models here.
class Proprietaire(models.Model):
    TYPE = (
        ("PROFESSIONNEL", 'PROFESSIONNEL'),
        ("PARTICULIER", 'PARTICULIER')
    )
    reference = models.CharField(max_length=100)
    type_proprietaire = models.CharField(max_length=100, choices=TYPE)
    nom_raison_sociale = models.CharField(max_length=255)
    nom_proprietaire = models.CharField(max_length=255, blank=True, null=True)
    tel_proprietaire = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    nom_responsable = models.CharField(max_length=100, blank=True, null=True)
    tel_responsable = models.CharField(max_length=100, blank=True, null=True)
    nom_gardien = models.CharField(max_length=100, blank=True, null=True)
    tel_gardien = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Propriétaires"
    def __str__(self):
        return self.reference + ' ' + self.nom_raison_sociale