FREEZING_POINT = 0
BOILING_POINT = 100


def state_water(temperature):
    """ Returns the state of the water given a temperature """
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif FREEZING_POINT < temperature < BOILING_POINT:
        return "Liquid"
    else:
        return "Gas"
