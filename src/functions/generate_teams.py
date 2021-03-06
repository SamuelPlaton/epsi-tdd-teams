from .determine_category import determine_category
import numpy as np
import itertools

def generate_teams(players):
    """generate_teams
    Return two arrays of players that is the most balancing according to the array given in parameter.
    :parameter  players   An array of players
    :return     two arrays of players
    """
    # return empty array if no players given
    if len(players) == 0:
        return [[], []]

    # setup vars for weight comparison
    first_team = []
    second_team = []
    correct_setup = []

    # generate all possible matchups with currently existing players
    teams = []
    for team in itertools.combinations(players, int(len(players)/2)):
        players_copy = []
        for player in players:
            players_copy.append(player)
        combination = []
        for player in team:
            players_copy.pop(players_copy.index(player))
        team = list(team)
        combination.append(team)
        combination.append(players_copy)
        teams.append(combination)
    
    # delete second half of teams array, to ensure non-duplication of matchups
    del teams[:int(len(teams)/2)]

    best_weight_difference = 100
    best_weight_difference_setup = None

    # divide all teams from their bynome group, and checks for weight category correspondance
    for matchup in teams:
        first_team = matchup[0]
        second_team = matchup[1]
        first_team_weight_average = sum(p.weight for p in first_team) / len(first_team)
        second_team_weight_average = sum(p.weight for p in second_team) / len(second_team)
        first_team_category = determine_category(first_team_weight_average)
        second_team_category = determine_category(second_team_weight_average)
        if first_team_category == second_team_category:
            correct_setup.append([first_team, second_team])
        elif abs(first_team_weight_average - second_team_weight_average) < best_weight_difference:
            best_weight_difference = abs(first_team_weight_average - second_team_weight_average)
            best_weight_difference_setup = [first_team, second_team]
        first_team = []
        second_team = []

    # setup vars for experience comparison
    best_experience_difference = 100
    best_setup = None

    # for each correct setup, get the best one
    for combination in correct_setup:
        first_team_experience_average = sum(p.experience for p in combination[0]) / len(combination[0])
        second_team_experience_average = sum(p.experience for p in combination[1]) / len(combination[1])
        experience_difference = abs(first_team_experience_average - second_team_experience_average)
        if experience_difference < best_experience_difference:
            best_experience_difference = experience_difference
            best_setup = combination
    if best_setup != None:
        return best_setup
    else:
        return best_weight_difference_setup