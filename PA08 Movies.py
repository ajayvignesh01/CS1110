# Ajay Chandrasekaran (HPD2DZ)

# list = ['movie name', 'gross earning', 'year', 'rating out of 10', 'number of ratings']
avengers_endgame = ['Avengers: Endgame', 2.797, 2019, 8.2, 532]
avengers_infinity_war = ['Avengers: Infinity War', 2.048, 2018, 7.6, 474]
the_avengers = ['The Avengers', 1.518, 2012, 8.0, 358]
avengers_age_of_ultron = ['Avengers: Age of Ultron', 1.405, 2015, 6.8, 37]
black_panther = ['Black Panther', 1.346, 2018, 8.3, 515]
incredibles_2 = ['Incredibles 2', 1.242, 2018, 7.84, 379]
iron_man_3 = ['Iron Man 3', 1.214, 2013, 7.0, 325]

# given list
movies_lst = [
    ["Avengers: Endgame", 2.797, 2019, 8.2, 532],
    ["Avengers: Infinity War", 2.048, 2018, 7.6, 474],
    ["The Avengers", 1.518, 2012, 8.0, 358],
    ["Avengers: Age of Ultron", 1.405, 2015, 6.8, 370],
    ["Black Panther", 1.346, 2018, 8.3, 515],
    ["Incredibles 2", 1.242, 2018, 7.84, 379],
    ["Iron Man 3", 1.214, 2013, 7.0, 325]
]


# helper functions
def get_name(movie):
    """ gets 0 index of the 1st movie list which contains movie name """
    return movie[0]


def get_gross(movie):
    """ gets 1st index of the 1st movie list which contains movie gross """
    return movie[1]


def get_rating(movie):
    """ gets 3rd index of the 1st movie list which contains movie rating """
    return movie[3]


def get_num_ratings(movie):
    """ gets 4th index of the 1st movie list which contains movie number of ratings """
    return movie[4]


# primary functions
def better_movies(movie_name, lst):
    """ finds which index/sublist movie_name is located within lst. Then runs through each sublist in lst.
    If rating > movie_name rating, the sublist is outputted into a new list """
    x = int()
    better_ratings_list = []
    while not lst[x][0] == movie_name:
        x += 1
    else:
        rating_to_beat = lst[x][3]
    for y in range(len(lst)):
        if lst[y][3] > rating_to_beat:
            better_ratings_list += [lst[y]]
    return better_ratings_list


def average(category, lst):
    """ determines the average of a given category by determining how many movies present,
     calculating the sum, then dividing by the number of movies present to give average"""
    avg_rating = 0
    if category == 'rating':
        for rating_1 in lst:
            avg_rating += rating_1[3]
        avg_rating /= len(lst)
        return avg_rating
    avg_gross = 0
    if category == 'gross':
        for gross_1 in lst:
            avg_gross += gross_1[1]
        avg_gross /= len(lst)
        return avg_gross
    avg_number_of_ratings_1 = 0
    if category == 'number of ratings':
        for number_of_ratings_1 in lst:
            avg_number_of_ratings_1 += number_of_ratings_1[4]
        avg_number_of_ratings_1 /= len(lst)
        return avg_number_of_ratings_1