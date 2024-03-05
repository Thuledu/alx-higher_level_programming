#!/usr/bin/python3
# A function that finds a peak in a list of unsorted integers.
def find_peak(list_of_integers):

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    midd_index = int(len(list_of_integers) / 2)

    if midd_index != len(list_of_integers) - 1:
        if list_of_integers[midd_index - 1] < list_of_integers[midd_index] and\
           list_of_integers[midd_index + 1] < list_of_integers[midd_index]:
            return list_of_integers[midd_index]
    else:
        if list_of_integers[midd_index - 1] < list_of_integers[midd_index]:
            return list_of_integers[midd_index]
        else:
            return list_of_integers[midd_index - 1]

    if list_of_integers[midd_index - 1] > list_of_integers[midd_index]:
        the_list = list_of_integers[0:midd_index]
    else:
        the_list = list_of_integers[midd_index + 1:]

    return find_peak(the_list)
