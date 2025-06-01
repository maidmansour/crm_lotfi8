from django.db import models

class Client(models.Model):
    TYPE = (
        ("PROFESSIONNEL", 'PROFESSIONNEL'),
        ("PARTICULIER", 'PARTICULIER')
    )
    reference = models.CharField(max_length=100)
    type_client = models.CharField(max_length=100, choices=TYPE)
    nom_raison_sociale = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=20, blank=True, null=True)
    nom_responsable = models.CharField(max_length=100, blank=True, null=True)
    tel_responsable = models.CharField(max_length=100, blank=True, null=True)
    
    
    class Meta:
        verbose_name_plural = "Clients"
    def __str__(self):
        return self.reference + ' ' + self.nom_raison_sociale