from django.db import models
from proprietes.models import Propriete
from clients.models import Client

class Operation(models.Model):
    
    STATUS = (
        ("LOCATION LONGUE DUREE", 'LOCATION LONGUE DUREE'),
        ("LOCATION COURTE DUREE", 'LOCATION COURTE DUREE'),
        ("FOND DE COMMERCE", 'FOND DE COMMERCE'),
        ("DROIT D'ENTREE", "DROIT D'ENTREE"),
        ("VENTE", 'VENTE')
    )
    DUREE = (
        ("FERME", 'FERME'),
        ("SIX MOIS FERME", 'SIX MOIS FERME'),
        ("SIX MOIS RENOUVELABLE", 'SIX MOIS RENOUVELABLE'),
        ("UNE ANNEE FERMEE", 'UNE ANNEE FERMEE'),
        ("UNE ANNEE RENOUVELABLE", 'UNE ANNEE RENOUVELABLE'),
    )

    date_operation = models.DateField(max_length=255)
    type_operation = models.CharField(max_length=50, choices=STATUS)
    propriete = models.ForeignKey(Propriete, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    prix_operation = models.IntegerField()
    duree_operation = models.CharField(max_length=200, choices=DUREE)
    monant_commission = models.IntegerField()
    numero_contrat = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Operation"
    def __str__(self):
        return self.propriete + ' CLIENT : ' + self.client