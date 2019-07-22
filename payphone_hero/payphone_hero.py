from math import ceil


def total_cost(calls):

    day_dict = {}

    for i in calls:
        date, time, sec = i.split(' ')
        minutes = ceil(int(sec) / 60)
        print(date, time, sec, minutes)
        day_dict[date] = day_dict.get(date, 0) + minutes

    return sum((2 * price - min(price, 100)) for price in day_dict.values())
