from django.db import models
import os
import uuid

def renommer_image_agent (instance, filename):
    print("====> Fonction de renommage appelée")  # test
    # extrait l'extension
    ext = filename.split('.')[-1]
    # génère un nom unique
    new_filename = f"{uuid.uuid4().hex}.{ext}"
    print("path", os.path.join('photos_agent/', new_filename))
    return os.path.join('photos_agent/', new_filename)

def renommer_image_intermidiaire (instance, filename):
    # extrait l'extension
    ext = filename.split('.')[-1]
    # génère un nom unique
    new_filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('photos_intermidiaire/', new_filename)

class Typebien(models.Model):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Types de Bien"
    def __str__(self):
        return self.title

class Secteur(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Secteurs"
    def __str__(self):
        return self.title
    
class Quartier(models.Model):
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Quartiers"
    def __str__(self):
        return self.title

class Residence(models.Model):
    title = models.CharField(max_length=200)
    address = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Résidences"
    def __str__(self):
        return self.title


class Soustypebien(models.Model):
    type_bien = models.ForeignKey(Typebien, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Sous Type de Bien"
    def __str__(self):
        return self.title

class Intermidiaire(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=renommer_image_intermidiaire, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Intermidiaires"
    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Agent(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=renommer_image_agent, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Agents"
    def __str__(self):
        return self.firstname + ' ' + self.lastname
    
