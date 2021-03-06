from classes import Category

def determine_category(weight):
    """determine_category
    Return a category depending on a weight given.
    :parameter  weight   A weight in kg (float)
    :return     a category Enum
    :exception  TypeError   If nor a float or int given
    """
    if weight < 52:
        return Category.FLY
    elif 52 <= weight < 57:
        return Category.FEATHER
    elif 57 <= weight < 63:
        return Category.LIGHT
    elif 63 <= weight < 69:
        return Category.WELTER
    elif 69 <= weight < 75:
        return Category.MEDIUM
    elif 75 <= weight < 81:
        return Category.MEDIUM_HEAVY
    elif 81 <= weight < 91:
        return Category.HEAVY
    elif weight >= 91:
        return Category.SUPER_HEAVY
    else:
        return TypeError