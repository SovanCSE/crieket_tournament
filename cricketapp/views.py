from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import TeamForm, PlayerForm, MatchesForm
from .models import Team, Player, Matches

"""
Below action used to create new team record
"""
class CreateTeam(CreateView):
    form_class = TeamForm
    template_name = 'teams/create_team.html'
    success_url = reverse_lazy('team_list')

"""
Below action used to update existence record by team id 
"""
class UpdateTeam(UpdateView):
    queryset = Team.objects.filter(is_active=True)
    form_class = TeamForm
    template_name = 'teams/update_team.html'
    success_url = reverse_lazy('team_list')

"""
Below action used to get active team records
"""
class TeamList(ListView):
    model = Team
    template_name = 'teams/team_list.html'

    def get_context_data(self, **kwargs):
        context = super(TeamList, self).get_context_data(**kwargs)
        team_list = self.model.objects.filter(is_active=True)
        page_no = self.request.GET.get('page', 1)
        paginator = Paginator(team_list, 5)
        team_list = paginator.get_page(page_no)
        context['team_list'] = team_list
        return context

"""
Below action used to delete single team record by team id
"""
def delete_team(request, id=None):
    if request.method == "POST":
        try:
            team = Team.objects.get(id=id)
            team.is_active = False
            team.save()
            messages.success(request, f'{team.name} deleted successfully')
            return redirect('team_list')
        except Team.DoesNotExist:
            messages.success(request, f'team data is not available')
            return redirect('team_list')
    else:
        return redirect('team_list')

"""
Below method used to get active player list 
"""
class PlayerList(ListView):
    model = Player
    template_name = 'players/player_list.html'
    context_object_name = "player_list_info"

    def get_context_data(self, **kwargs):
        context = super(PlayerList, self).get_context_data(**kwargs)
        player_list = self.model.objects.filter(is_active=True)
        page_no = self.request.GET.get('page', 1)
        paginator = Paginator(player_list, 10)
        player_list = paginator.get_page(page_no)
        context['player_list_info'] = player_list
        return context

"""
Below action used to retrieve players for a particular team
"""
class RetrieveMatchPlayers(DetailView):
    model = Player
    template_name = 'players/player_list.html'
    slug_field = 'team_id'
    slug_url_kwarg = 'team_id'

    def get_object(self, queryset=None):
        if not queryset:
            return []
        return queryset

    def get_context_data(self, **kwargs):
        context = super(RetrieveMatchPlayers, self).get_context_data(**kwargs)
        self.team_id = self.kwargs.get('team_id')
        self.team_name = get_object_or_404(Team, id=self.team_id)
        players = self.model.objects.filter(team_id=self.team_id, is_active=True)
        context['player_list_info'] = players
        context['team_name'] = self.team_name
        return context

"""
Below action used to add new player record
"""
class AddPlayer(CreateView):
    form_class = PlayerForm
    template_name = 'players/add_player.html'
    success_url = reverse_lazy('player_list')

"""
Below action used to update player record by player id
"""
class UpdatePlayer(UpdateView):
    queryset = Player.objects.filter(is_active=True)
    form_class = PlayerForm
    template_name = 'players/update_player.html'
    success_url = reverse_lazy('player_list')

"""
Below action used to delete a player record by player id
"""
def delete_player(request, id):
    if request.method == "POST":
        try:
            player = Player.objects.get(id=id)
            player.is_active = False
            player.save()
            messages.success(request, f'Player {player.first_name} {player.last_name} deleted '
                                      f'successfully from {player.team.name} team')
            return redirect('player_list')
        except Team.DoesNotExist:
            messages.success(request, f'player data is not available')
            return redirect('player_list')
    else:
        return redirect('player_list')

"""
Below action used to add new match details
"""
class ADDMatch(CreateView):
    form_class = MatchesForm
    template_name = 'matches/add_macthes.html'
    success_url = reverse_lazy('match_list')

"""
Below action used to update a existence  match by macth id
"""
class UpdateMacth(UpdateView):
    form_class = MatchesForm
    queryset = Matches.objects.filter(is_active=True)
    template_name = 'matches/update_matches.html'
    success_url = reverse_lazy('match_list')

"""
Below action used to get all match records
"""
class MatchList(ListView):
    model = Matches
    template_name = 'matches/matches_list.html'
    context_object_name = "match_list"

    def get_context_data(self, **kwargs):
        context = super(MatchList, self).get_context_data(**kwargs)
        match_list = self.model.objects.filter(is_active=True)
        page_no = self.request.GET.get('page', 1)
        paginator = Paginator(match_list, 6)
        match_list = paginator.get_page(page_no)
        context['match_list'] = match_list
        return context

"""
Below action used to delete a match record from my macth id
"""
def delete_match(request, pk=None):
    if request.method == "POST":
        try:
            match = Matches.objects.get(id=pk)
            match.is_active= False
            match.save()
            messages.success(request, f'Mathch record is deleted successfully')
            return redirect('match_list')
        except Matches.DoesNotExist:
            messages.success(request, f'match record is not available')
            return redirect('match_list')
    else:
        return redirect('match_list')

"""
Below action used to get all matches history for particular team
"""
class TeamMacthesList(DetailView):
    model = Matches
    template_name = 'matches/matches_list.html'
    slug_field = 'team_id'
    slug_url_kwarg = 'team_id'


    def get_object(self, queryset=None):
        if not queryset:
            return []
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TeamMacthesList, self).get_context_data(**kwargs)
        self.team_id = self.kwargs.get('team_id')
        self.team_name = get_object_or_404(Team, id=self.team_id)
        matches = self.model.objects.filter( (Q(first_teamname_id=self.team_id) | Q(
            second_teamname_id=self.team_id)) & (Q(is_active=True)) )
        context['match_list'] = matches
        context['team_name'] = self.team_name
        return context

"""
Below action is used get points table results over all matches
"""
def get_points_table(request):
    team_list = Team.objects.filter(is_active=True)
    point_table_details = []
    for team_info in team_list:
        total_played_macthes = Matches.objects.filter( (Q(first_teamname_id=team_info.id) | Q(
            second_teamname_id=team_info.id)) & (Q(is_active=True))).count()
        total_win = Matches.objects.filter(match_winner=team_info.name,is_active=True).count()
        total_draw = Matches.objects.filter((Q(first_teamname_id=team_info.id) | Q(
            second_teamname_id=team_info.id)) & (Q(match_winner='Draw Match') & (Q(
            is_active=True)))).count()
        total_loss = total_played_macthes - (total_win + total_draw)
        total_point = total_win*2 + total_draw*1
        point_table_details.append({
                'id':team_info.id,
                'name':team_info.name,
                'logo_url':team_info.logo_url,
                'total_match':total_played_macthes if total_played_macthes else 0,
                'total_win':total_win if total_win else 0,
                'total_loss':total_loss if total_loss else 0,
                "total_draw":total_draw if total_draw else 0,
                'total_point':total_point if total_point else 0})
    point_table_details = sorted(point_table_details, key=lambda item: item.get('total_point'),
                                 reverse=True)

    point_table_paginator = Paginator(point_table_details, 5)
    point_table_details = point_table_paginator.get_page(request.GET.get('page', 1))
    return render(request, 'pointstable/pointstable_list.html',{"point_table_details":point_table_details})
