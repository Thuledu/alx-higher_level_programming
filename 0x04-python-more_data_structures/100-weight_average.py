#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    product_sum = sum(map(lambda x: x[0] * x[1], my_list))

    weight_sum = sum(map(lambda x: x[1], my_list))

    weighted_average = product_sum / weight_sum

    return weighted_average
