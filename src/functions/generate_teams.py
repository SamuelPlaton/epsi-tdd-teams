from .determine_category import determine_category
import numpy as np

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

    # Shuffle 1000 possibilities and retrieve correct setups
    i = 0
    while i < 300:
        np.random.shuffle(players)
        # dispatch users
        for player in players:
            if len(first_team) <= len(second_team):
                first_team.append(player)
            else:
                second_team.append(player)
        first_team_category = determine_category(sum(p.weight for p in first_team) / len(first_team))
        second_team_category = determine_category(sum(p.weight for p in second_team) / len(second_team))
        if first_team_category == second_team_category:
            correct_setup.append([first_team, second_team])
        i = i + 1
        first_team = []
        second_team = []


    # setup vars for experience comparison
    best_experience_difference = 100
    best_setup = [[], []]

    # for each correct setup, get the best one
    for combination in correct_setup:
        first_team_experience_average = sum(p.experience for p in combination[0]) / len(combination[0])
        second_team_experience_average = sum(p.experience for p in combination[1]) / len(combination[1])
        experience_difference = abs(first_team_experience_average - second_team_experience_average)
        if experience_difference < best_experience_difference:
            best_experience_difference = experience_difference
            best_setup = combination
    return best_setup

