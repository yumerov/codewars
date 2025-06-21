# https://www.codewars.com/kata/human-readable-time/train/python


def fmt(number): return "0" + str(number) if number < 10 else str(number)


def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    return "{}:{}:{}".format(fmt(hours), fmt(minutes), fmt(seconds))

