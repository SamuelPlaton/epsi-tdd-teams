from functions import determine_category


def compare_teams_weight(team_1, team_2):
    """compare_teams_weight
    Return a comparaison between two teams categories
    :parameter  team_1 team_2   Two teams objects
    :return     boolean
    """
    # Retrieve teams weight
    first_team_weight = sum(p.weight for p in team_1)
    second_team_weight = sum(p.weight for p in team_2)
    # Determine their category
    first_team_category = determine_category(first_team_weight / len(team_1.first_team))
    second_team_category = determine_category(second_team_weight / len(team_2.second_team))
    # Assert that they are on the same category
    if first_team_category == second_team_category:
        return True
    else:
        return False
