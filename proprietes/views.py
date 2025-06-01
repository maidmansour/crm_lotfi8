import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from .models import Propriete,  Image
from .forms import ProprieteForm, RechercheForm
from settings.models import Secteur, Quartier, Residence
from django.http import JsonResponse, Http404
import json

@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    )
def list(request):
    if request.POST:
      recherche_form = RechercheForm(request.POST)
      list_proprietes = Propriete.objects.all()
      if recherche_form.is_valid():
        type_bien = recherche_form.cleaned_data['type_bien']
        type_operation = recherche_form.cleaned_data['type_operation']
        secteur = recherche_form.cleaned_data['secteur']
        reference = recherche_form.cleaned_data['reference']
        proprietaire = recherche_form.cleaned_data['proprietaire']
        residence = recherche_form.cleaned_data['residence']
        intermidiaire = recherche_form.cleaned_data['intermidiaire']
        agent = recherche_form.cleaned_data['agent']
        bedrooms_min = recherche_form.cleaned_data['bedrooms_min']
        bedrooms_max = recherche_form.cleaned_data['bedrooms_max']
        price_min = recherche_form.cleaned_data['price_min']
        price_max = recherche_form.cleaned_data['price_max']
        exclusive = recherche_form.cleaned_data['exclusive']
        

        if type_bien:
          list_proprietes = list_proprietes.filter(type_bien=type_bien)
        
        if type_operation:
          list_proprietes = list_proprietes.filter(type_operation=type_operation)

        if secteur:
          list_proprietes = list_proprietes.filter(secteur=secteur)

        if reference:
          list_proprietes = list_proprietes.filter(reference=reference)

        if proprietaire:
          list_proprietes = list_proprietes.filter(proprietaire=proprietaire)

        if residence:
          list_proprietes = list_proprietes.filter(residence=residence)

        if intermidiaire:
          list_proprietes = list_proprietes.filter(intermidiaire=intermidiaire)
        
        if agent:
          list_proprietes = list_proprietes.filter(agent=agent)

        if bedrooms_min and bedrooms_max:
          if int(bedrooms_min) <= int(bedrooms_max):
            list_proprietes = list_proprietes.filter(global_bedrooms__gte=int(bedrooms_min), global_bedrooms__lte=int(bedrooms_max))
        
        if price_min and price_max :
            if int(price_min) <= int(price_max):
              list_proprietes = list_proprietes.filter(price__gte=int(price_min), price__lte=int(price_max))
        
        
        list_proprietes = list_proprietes.filter(exclusive=exclusive)

      context = {
          'list_proprietes':list_proprietes,
          'recherche_form': recherche_form
      }
    else:
      recherche_form = RechercheForm
      list_proprietes = Propriete.objects.all()
      context = {
          'list_proprietes':list_proprietes,
          'recherche_form': recherche_form
      }
    return render(request, 'propriete/list.html', context=context)


@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    ) 
def propriete_edit (request, pk=None):
  if request.POST:
    
    if not pk:
        files = request.FILES.getlist('images[]')
        propriete_form = ProprieteForm(request.POST)
        
        if propriete_form.is_valid():
          propriete=propriete_form.save()

          for file in files:
            file_name = file.name
            new_file_name = f"{propriete.reference}__{file_name}"
            file.name = new_file_name
            Image.objects.create(pic=file, propriete=propriete)

        else:
          propriete_form = ProprieteForm(request.POST)
          
          context = {
            'propriete_form':propriete_form,
            'images': files
          }
          return render(request, 'propriete/edit.html', context)

        
    else:
        propriete = Propriete.objects.get(pk=pk)
        files = request.FILES.getlist('images[]')
        propriete_form = ProprieteForm(request.POST, instance=propriete)
        if propriete_form.is_valid():
          propriete = propriete_form.save()
          

          if files:
            
            images = Image.objects.filter(propriete=propriete)
            for image in images:
              # Chemin du fichier à supprimer
              file_path = os.path.join(settings.MEDIA_ROOT, image.pic.name)

              # Supprimer le fichier du système de fichiers
              if os.path.isfile(file_path):
                  os.remove(file_path)

              # Supprimer l'entrée de l'image dans la base de données
              image.delete()

         
            for file in files:
              file_name = file.name
              new_file_name = f"{propriete.reference}__{file_name}"
              file.name = new_file_name
              Image.objects.create(pic=file, propriete=propriete)
        else:
          propriete_form = ProprieteForm(request.POST)
         
          context = {
            'propriete_form':propriete_form,
            'pk':pk,
            'images':files
          }
          return render(request, 'propriete/edit.html', context)
         
                                      
          
    return redirect('list-proprietes')
  else:   

    if pk:
      propriete = get_object_or_404(Propriete, pk=pk)
      propriete_form = ProprieteForm(instance=propriete)
      images = Image.objects.filter(propriete=propriete)
      context = {
        'propriete_form':propriete_form,
        'images': images
 
      }
    else:
      propriete_form = ProprieteForm

      context = {
        'propriete_form':propriete_form,

      }
  return render(request, 'propriete/edit.html', context)


def delete_image(request, image_id):
    if request.method == 'POST':
        # Récupérer l'image à partir de son ID
        image = get_object_or_404(Image, id=image_id)

        # Chemin du fichier à supprimer
        file_path = os.path.join(settings.MEDIA_ROOT, image.pic.name)

        # Supprimer le fichier du système de fichiers
        if os.path.isfile(file_path):
            os.remove(file_path)

        # Supprimer l'entrée de l'image dans la base de données
        image.delete()

        # Retourner une réponse JSON indiquant le succès
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)


def quartiers_load(request):
  if request.method == "POST":
      data = json.loads(request.body)
      secteur= data.get('secteur', '')
      quartier_list = []

      secteur = Secteur.objects.get(pk=secteur) if secteur else None
      if secteur:
        
        quartiers = Quartier.objects.filter(secteur=secteur)
        for quartier in quartiers:
          partObj = {}
          partObj["id"] = quartier.id
          partObj["title"] = quartier.title
          quartier_list.append(partObj)
        
      return JsonResponse({"quartier_list":quartier_list})
      
  else:
    raise Http404()

def address_load(request):
  if request.method == "POST":
      data = json.loads(request.body)
      residence_id= data.get('residence', '')
      quartier_list = []

      residence = Residence.objects.get(pk=residence_id) if residence_id else None
      address = ""
      if residence:
          address=residence.address
        
      return JsonResponse({"address":address})
      
  else:
    raise Http404()