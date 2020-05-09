from django import forms
from .models import Team, Player, Matches
from crispy_forms.helper import  FormHelper

class TeamForm(forms.ModelForm):
    helper = FormHelper()
    helper.label_class = 'font-weight-bold font-italic'

    class Meta:
        model = Team
        # fields = ['name', 'logo_url', 'club_state']
        fields ='__all__'

class PlayerForm(forms.ModelForm):
    class Meta:
        model= Player
        fields = '__all__'

class MatchesForm(forms.ModelForm):
    team_list = [('---------', "---------")]
    try:
        teams = Team.objects.values('name')
        team_list = [(info.get('name'), info.get('name')) for info in teams]
        team_list.insert(0, ("Draw Match", "Draw Match"))
        team_list.insert(0,('---------', "---------"))
    except Exception as e:
        pass
    match_winner = forms.ChoiceField(choices=team_list)

    class Meta:
        model= Matches
        fields="__all__"

    def clean(self):
        cleaned_data = super(MatchesForm,self).clean()
        first_teamname = str(cleaned_data.get('first_teamname'))
        second_teamname = str(cleaned_data.get('second_teamname'))
        match_winner = cleaned_data.get('match_winner')
        if first_teamname == second_teamname:
            raise forms.ValidationError("Please, select two different team for this match")
        if match_winner not in [first_teamname, second_teamname, 'Draw Match']:
            if match_winner in '---------':
                raise forms.ValidationError('Please select a match winner')
            raise forms.ValidationError('Selected match winner is not valid')


# class PointsTableForm(forms.ModelForm):
#     class Meta:
#         model= PointsTable
#         fields="__all__"

    # def clean(self):
    #     pass

