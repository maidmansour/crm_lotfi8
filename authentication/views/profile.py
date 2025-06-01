from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import JsonResponse, Http404
from django.contrib import messages
from django.contrib.auth.models import User
from ..utils import EmailThread
from ..models import Profile, Team
from ..forms import ProfileForm, UserForm, TeamForm, MyProfileForm
from django.template.loader import render_to_string
from django.db.models.functions import Lower
from django.contrib.auth import update_session_auth_hash
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from ..forms import CustomUserForm, UserProfileForm
from django.contrib.auth import update_session_auth_hash




@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    )
def list(request):
    list_users = User.objects.filter(is_superuser=False, is_active=True)
    context = {
        'list_users':list_users
    }
    return render(request, 'auth/list.html', context=context)

@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    )



def account_edit(request, pk=None):
    if pk:
        user = get_object_or_404(User, pk=pk)
    else:
        user = None

    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users-list')  # à adapter selon ton app
    else:
        form = CustomUserForm(instance=user)

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'auth/edit.html', context)


@login_required
def profile_edit(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user)  # ← Garde l'utilisateur connecté même après avoir changé son mot de passe
            return redirect('profile_edit')  # ou vers une page de confirmation
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'auth/profile_form.html', {'form': form})

@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    )
def team_add(request):
    if request.method == "POST":
        data = json.loads(request.body)
        team_title= data.get('team_title', '')
        category= data.get('category', '')
        response = False
        team_id = None       
        if team_title != '' and category != '':
  
            team = Team.objects.annotate(team_lower=Lower('team_title')).filter(team_lower=team_title.lower(),category=category, company=config.company )
            
            if not team.exists():
                team = Team.objects.create(team_title=team_title,category=category, company=config.company)
                response = True
                team_id = team.pk

        return JsonResponse({"response": response, "team_id": team_id})
    else:
        raise Http404()