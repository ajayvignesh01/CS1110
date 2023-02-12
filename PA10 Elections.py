# Ajay Chandrasekaran (HPD2DZ)

election_results = {}

college = {'Virginia': 13, 'Ohio': 18, 'Minnesota': 10, 'Alabama': 9, 'Maine': 4}


def add_state(name, votes):
    most_votes = max(votes, key=votes.get)
    election_results[name] = most_votes


def winner(college):
    global election_results
    total_votes = {}
    winner_text = 'No Winner'
    for keys, values in election_results.items():
        if values in total_votes:
            total_votes[values] += college.get(keys, 0)
        elif values not in total_votes:
            total_votes[values] = college.get(keys, 0)
    electors_to_win = (sum(total_votes.values())) * 0.5
    for keys, values in total_votes.items():
        if values > electors_to_win:
            winner_text = keys
    return winner_text


def clear():
    global election_results
    election_results = {}