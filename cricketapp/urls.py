"""cricket_tournaments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [

    path('', TeamList.as_view(), name='team_list'),
    path('create-team/', CreateTeam.as_view(), name='create_team'),
    path('update-team/<int:pk>/', UpdateTeam.as_view(), name='update_team'),
    path('delete-team/<int:id>/', delete_team, name='delete_team'),

    path('add-player/', AddPlayer.as_view(), name='add_player'),
    path('update-player/<int:pk>/', UpdatePlayer.as_view(), name='update_player'),
    path('player-list/', PlayerList.as_view(), name='player_list'),
    path('delete-player/<int:id>/', delete_player, name='delete_player'),

    path('add-match/', ADDMatch.as_view(), name='add_match'),
    path('update-match/<int:pk>/', UpdateMacth.as_view(), name='update_match'),
    path('match-list/', MatchList.as_view(), name='match_list'),
    path('delete-match/<int:pk>/', delete_match, name='delete_match'),

    path('retrieve-player/<int:team_id>/', RetrieveMatchPlayers.as_view(), name='retrieve_player'),
    path('team-matches/<int:team_id>/', TeamMacthesList.as_view(), name='team_matches'),

    path('points-table/', get_points_table, name="points_table")

]
