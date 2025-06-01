from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from .models import Residence, Agent, Intermidiaire, Typebien, Soustypebien, Secteur, Quartier
from .forms import ResisenceForm, AgentForm, IntermidiaireForm,TypebienForm, SoustypebienForm, SecteurForm, QuartierForm
from django.http import JsonResponse

@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    )
def list(request):
    residence_form = ResisenceForm
    agent_form = AgentForm
    intermidiaire_form = IntermidiaireForm
    type_bien_form = TypebienForm
    sous_type_bien_form = SoustypebienForm
    secteur_form = SecteurForm
    list_residences = Residence.objects.all().order_by('title')
    list_agents = Agent.objects.all().order_by('firstname')
    list_intermidiaires = Intermidiaire.objects.all().order_by('firstname')
    list_type_biens = Typebien.objects.all().order_by('title')
    list_sous_type_biens = Soustypebien.objects.all().order_by('title')
    list_secteurs = Secteur.objects.all().order_by('title')
    list_quartiers = Quartier.objects.all().order_by('title')

    context = {
        'list_residences':list_residences,
        'list_quartiers':list_quartiers,
        'list_agents':list_agents,
        'list_intermidiaires':list_intermidiaires,
        'list_type_biens':list_type_biens,
        'list_sous_type_biens':list_sous_type_biens,
        'list_secteurs':list_secteurs,
        'residence_form': residence_form,
        'agent_form': agent_form,
        'sous_type_bien_form': sous_type_bien_form,
        'intermidiaire_form': intermidiaire_form,
        'type_bien_form': type_bien_form,
        'secteur_form': secteur_form,
    }
      
    return render(request, 'setting/list.html', context=context)



@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    ) 
def secteur_edit (request, pk=None):
    if request.POST:
    
        secteur_form = SecteurForm(request.POST)
        if not pk:
       
            if secteur_form.is_valid():
        
                secteur_form.save()

                return redirect('list-settings')

            else :
            
                context = {
                    'secteur_form':secteur_form,
                }
        
                return render(request, 'setting/secteur_edit.html', context)

        else:
            secteur = Secteur.objects.get(pk=pk)
            secteur_form = SecteurForm(request.POST, instance=secteur)
            if secteur_form.is_valid():

                secteur_form.save()

                return redirect('list-settings')
            
            else :
                context = {
                    'secteur_form':secteur_form,
                    'pk':pk,
                }
        
                return render(request, 'setting/secteur_edit.html', context)
    
    else :
        if pk:
            secteur = get_object_or_404(Secteur, pk=pk)
            secteur_form = SecteurForm(instance=secteur)
      
            context = {
                'secteur_form':secteur_form,        
            }
        else:
            secteur_form = SecteurForm

            context = {
                'secteur_form':secteur_form,

            }

        return render(request, 'setting/secteur_edit.html', context)
           
          
      

   


@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    ) 
def type_bien_edit (request, pk=None):
    if request.POST:
    
        type_bien_form = TypebienForm(request.POST)
        if not pk:
       
            if type_bien_form.is_valid():
        
                type_bien_form.save()

                return redirect('list-settings')

            else :
            
                context = {
                    'type_bien_form':type_bien_form,
                }
        
                return render(request, 'setting/type_bien_edit.html', context)

        else:
            type_bien = Typebien.objects.get(pk=pk)
            type_bien_form = TypebienForm(request.POST, instance=type_bien)
            if type_bien_form.is_valid():

                type_bien_form.save()

                return redirect('list-settings')
            
            else :
                context = {
                    'type_bien_form':type_bien_form,
                    'pk':pk,
                }
        
                return render(request, 'setting/type_bien_edit.html', context)
    
    else :
        if pk:
            type_bien = get_object_or_404(Typebien, pk=pk)
            type_bien_form = TypebienForm(instance=type_bien)
      
            context = {
                'type_bien_form':type_bien_form,        
            }
        else:
            type_bien_form = TypebienForm

            context = {
                'type_bien_form':type_bien_form,

            }

        return render(request, 'setting/type_bien_edit.html', context)
           
          
      

   


@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    ) 
def sous_type_bien_edit (request, pk=None):
    if request.POST:
    
        sous_type_bien_form = SoustypebienForm(request.POST)
        if not pk:
       
            if sous_type_bien_form.is_valid():
        
                sous_type_bien_form.save()

                return redirect('list-settings')

            else :
            
                context = {
                    'sous_type_bien_form':sous_type_bien_form,
                }
        
                return render(request, 'setting/sous_type_bien_edit.html', context)

        else:
            sous_type_bien = Soustypebien.objects.get(pk=pk)
            sous_type_bien_form = SoustypebienForm(request.POST, instance=sous_type_bien)
            if sous_type_bien_form.is_valid():

                sous_type_bien_form.save()

                return redirect('list-settings')
            
            else :
                context = {
                    'sous_type_bien_form':sous_type_bien_form,
                    'pk':pk,
                }
        
                return render(request, 'setting/sous_type_bien_edit.html', context)
    
    else :
        if pk:
            sous_type_bien = get_object_or_404(Soustypebien, pk=pk)
            sous_type_bien_form = SoustypebienForm(instance=sous_type_bien)
      
            context = {
                'sous_type_bien_form':sous_type_bien_form,        
            }
        else:
            sous_type_bien_form = SoustypebienForm

            context = {
                'sous_type_bien_form':sous_type_bien_form,

            }

        return render(request, 'setting/sous_type_bien_edit.html', context)
           
          
      


@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    ) 
def quartier_edit (request, pk=None):
    if request.POST:
    
        quartier_form = QuartierForm(request.POST)
        if not pk:
       
            if quartier_form.is_valid():
        
                quartier_form.save()

                return redirect('list-settings')

            else :
            
                context = {
                    'quartier_form':quartier_form,
                }
        
                return render(request, 'setting/quartier_edit.html', context)

        else:
            quartier = Quartier.objects.get(pk=pk)
            quartier_form = QuartierForm(request.POST, instance=quartier)
            if quartier_form.is_valid():

                quartier_form.save()

                return redirect('list-settings')
            
            else :
                context = {
                    'quartier_form':quartier_form,
                    'pk':pk,
                }
        
                return render(request, 'setting/quartier_edit.html', context)
    
    else :
        if pk:
            quartier = get_object_or_404(Quartier, pk=pk)
            quartier_form = QuartierForm(instance=quartier)
      
            context = {
                'quartier_form':quartier_form,        
            }
        else:
            quartier_form = QuartierForm

            context = {
                'quartier_form':quartier_form,

            }

        return render(request, 'setting/quartier_edit.html', context)
           
          
      
   

@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    ) 
def agent_edit (request, pk=None):
    if request.POST:
    
        agent_form = AgentForm(request.POST, request.FILES)
        if not pk:
       
            if agent_form.is_valid():
                agent = agent_form.save(commit=False)
                agent.save()  # ← ici,

                return redirect('list-settings')

            else :
            
                context = {
                    'agent_form':agent_form,
                }
        
                return render(request, 'setting/agent_edit.html', context)

        else:
            agent = Agent.objects.get(pk=pk)
            agent_form = AgentForm(request.POST,  request.FILES, instance=agent)
            if agent_form.is_valid():

                agent = agent_form.save(commit=False)
                agent.save()  # ← ici,

                return redirect('list-settings')
            
            else :
                context = {
                    'agent_form':agent_form,
                    'pk':pk,
                }
        
                return render(request, 'setting/agent_edit.html', context)
    
    else :
        if pk:
            agent = get_object_or_404(Agent, pk=pk)
            agent_form = AgentForm(instance=agent)
      
            context = {
                'agent_form':agent_form,        
            }
        else:
            agent_form = AgentForm

            context = {
                'agent_form':agent_form,

            }

        return render(request, 'setting/agent_edit.html', context)
           
          
      




@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    ) 
def intermidiaire_edit (request, pk=None):
    if request.POST:
    
        intermidiaire_form = IntermidiaireForm(request.POST,  request.FILES)
        if not pk:
       
            if intermidiaire_form.is_valid():
                intermidiaire = intermidiaire_form.save(commit=False)
                intermidiaire.save()  # ← ici,
                intermidiaire_form.save()

                return redirect('list-settings')

            else :
            
                context = {
                    'intermidiaire_form':intermidiaire_form,
                }
        
                return render(request, 'setting/intermidiaire_edit.html', context)

        else:
            intermidiaire = Intermidiaire.objects.get(pk=pk)
            intermidiaire_form = IntermidiaireForm(request.POST,  request.FILES, instance=intermidiaire)
            if intermidiaire_form.is_valid():

                intermidiaire = intermidiaire_form.save(commit=False)
                intermidiaire.save()  # ← ici,
                intermidiaire_form.save()

                return redirect('list-settings')
            
            else :
                context = {
                    'intermidiaire_form':intermidiaire_form,
                    'pk':pk,
                }
        
                return render(request, 'setting/intermidiaire_edit.html', context)
    
    else :
        if pk:
            intermidiaire = get_object_or_404(Intermidiaire, pk=pk)
            intermidiaire_form = IntermidiaireForm(instance=intermidiaire)
      
            context = {
                'intermidiaire_form':intermidiaire_form,        
            }
        else:
            intermidiaire_form = IntermidiaireForm

            context = {
                'intermidiaire_form':intermidiaire_form,

            }

        return render(request, 'setting/intermidiaire_edit.html', context)
           
          
      

   

@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    ) 
def residence_edit (request, pk=None):
    if request.POST:
    
        residence_form = ResisenceForm(request.POST)
        if not pk:
       
            if residence_form.is_valid():
        
                residence_form.save()

                return redirect('list-settings')

            else :
            
                context = {
                    'residence_form':residence_form,
                }
        
                return render(request, 'setting/residence_edit.html', context)

        else:
            residence = Residence.objects.get(pk=pk)
            residence_form = ResisenceForm(request.POST, instance=residence)
            if residence_form.is_valid():

                residence_form.save()

                return redirect('list-settings')
            
            else :
                context = {
                    'residence_form':residence_form,
                    'pk':pk,
                }
        
                return render(request, 'setting/residence_edit.html', context)
    
    else :
        if pk:
            residence = get_object_or_404(Residence, pk=pk)
            residence_form = ResisenceForm(instance=residence)
      
            context = {
                'residence_form':residence_form,        
            }
        else:
            residence_form = ResisenceForm

            context = {
                'residence_form':residence_form,

            }

        return render(request, 'setting/residence_edit.html', context)
           
          
      

   