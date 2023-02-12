# Ajay Chandrasekaran (HPD2DZ)

def card_to_value(card):
    if card == 'A':
        return 1
    elif card == '1':
        return 1
    elif card == '2':
        return 2
    elif card == '3':
        return 3
    elif card == '4':
        return 4
    elif card == '5':
        return 5
    elif card == '6':
        return 6
    elif card == '7':
        return 7
    elif card == '8':
        return 8
    elif card == '9':
        return 9
    elif card == 'T' or card == 'J' or card == 'Q' or card == 'K':
        return 10
    elif card == 'E': # Kind of added my own thing here so that I can get the soft_score(hand) function working
        return 11


def hard_score(hand):
    value_hard = int()
    for i in range(len(hand)):
        value_hard += card_to_value((hand[i]))
    return value_hard


def soft_score(hand):
    value_soft = int()
    hand_modified = hand.replace("A", "E", 1)
    for i in range(len(hand_modified)):
        value_soft += card_to_value((hand_modified[i]))
    return value_soft
