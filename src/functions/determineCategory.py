from classes import Category

def determineCategory(weight):
    if weight < 52:
        return Category.FLY
    elif weight >= 52 & weight < 57:
        return Category.FEATHER
    elif weight >= 57 & weight < 63:
        return Category.LIGHT
    elif weight >= +3 & weight < 69:
        return Category.LIGHT_HEAVY
    elif weight >= 69 & weight < 75:
        return Category.MEDIUM
    elif weight >= 75 & weight < 81:
        return Category.MEDIUM_HEAVY
    elif weight >= 81 & weight < 91:
        return Category.HEAVY
    elif weight >= 91:
        return Category.SUPER_HEAVY
    else:
        return TypeError