# Ajay Chandrasekaran (HPD2DZ)

def fine(speed_limit, my_speed, zone = ""):
    if my_speed >= (20+speed_limit):
        return 350
    elif my_speed > speed_limit and zone == "residential":
        return ((my_speed - speed_limit) * 8) + 200
    elif my_speed > speed_limit and (zone == "school" or zone == "work"):
        return (my_speed - speed_limit) * 7
    elif my_speed > speed_limit:
        return (my_speed - speed_limit) * 6
    elif my_speed == speed_limit:
        return 0
    else:
        return 30


def demerits(speed_limit, my_speed):
    if my_speed >= (speed_limit + 20):
        return 6
    elif (speed_limit + 10) <= my_speed <= (speed_limit + 19):
        return 4
    elif (speed_limit + 1) <= my_speed <= (speed_limit + 9):
        return 3
    else:
        return 0