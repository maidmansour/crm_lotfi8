from .views import auth, profile
from django.urls import path, include
from django.urls import re_path
from dashboard.views import home
urlpatterns = [
    
    path('', home, name='home'),
    path('login/', auth.LoginView.as_view(), name='login'),
    path("logout/", auth.LogoutView.as_view(), name='logout'),
    path("reset-password/", auth.PasswordResetView.as_view(),
         name="reset-password"),
    path('change-password/<uidb64>/<token>',
         auth.CompletePasswordChangeView.as_view(), name='change-password'),
     path("edit/<pk>", profile.profile_edit, name='profile-edit'),
     path("edit/", profile.profile_edit, name='profile-edit'),
     path("my-profile/", profile.profile_edit, name='profile_edit'),
     path("team/add", profile.team_add, name="add-team"),
     path("account-edit", profile.account_edit, name="account-edit"),
     path("account-edit/<pk>", profile.account_edit, name="account-edit"),
     path("list-users", profile.list, name="users-list"),
     
]