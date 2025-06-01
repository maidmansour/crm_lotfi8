from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME

@user_passes_test(
        lambda u: u.is_authenticated and not u.is_superuser,
        login_url='login',
        redirect_field_name=REDIRECT_FIELD_NAME
    )
def home(request):

    return render(request, 'dashboard/home.html')
