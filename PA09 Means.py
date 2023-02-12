# Ajay Chandrasekaran (HPD2DZ)

# given sample list
cs = [[614, 88, 144],
      [534, 59, 148],
      [0, 0, 0],
      [682, 77, 146],
      [501, 93, 136],
      [44, 0, 0]]


# primary functions
def mean_all(table):
    """ Takes sum of each sublist and adds them together. Then, divides total sum by 'area of list' (length * width =
    total numbers in list) to determine mean"""
    average_all = float()
    for x in range(len(table)):
        average_all += sum(table[x])
    average_all /= (len(table) * len(table[0]))
    return average_all


def mean_by_row(table):
    """ Creates a new list (sum_row) with sums of rows (each sublist is a row). Then divides each sum by the amount of
    numbers in a sublist (row) and puts these values into a new list (avg_row) to output the mean of rows"""
    sum_row = []
    avg_row = []
    for y in range(len(table)):
        sum_row.append(float(sum(table[y])))
    for z in sum_row:
        avg_row.append(z / len(table[0]))
    return avg_row


def mean_by_col(table):
    """ Extracts all the values from sublists in a given list/table into a new list (all_values). Then, depending on the
    length of each row (z), creates a new sublist within a new list (column_sublists) based on every nth (z) value.
    Finally, sums up each sublist (column) and divides by the length of the column to produce column_averages list.
    In a nutshell, this function converts a column into a sublist to then find average of using the aid of sum() """
    all_values = []
    column_sublists = []
    column_averages = []
    for x in range(len(table)):
        for y in range(len(table[0])):
            all_values.append(table[x][y])
    for z in range(len(table[0])):
        column_sublists.append(all_values[z::(len(table[0]))])
    for c in range(len(table[0])):
        column_averages.append((sum(column_sublists[c])) / len(table))
    return column_averages


# Another way to do mean_all, this time using nested loops
'''
def mean_all(table):
    all_values = []
    mean = float()
    for x in range(len(table)):
        for y in range(len(table[0])):
            all_values.append(table[x][y])
    mean += (sum(all_values)) / (len(table) * len(table[0]))
    return mean
'''