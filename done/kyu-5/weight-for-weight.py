# https://www.codewars.com/kata/weight-for-weight/train/python


def weight_of_weight(weight): return sum([int(digit) for digit in weight])


def order_weight(weights):
    weights_values = sorted(weights.split(" "))

    return " ".join(sorted(weights_values, key=weight_of_weight))