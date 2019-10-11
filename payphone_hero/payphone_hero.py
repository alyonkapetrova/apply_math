# -*- coding: utf-8 -*-

import csv
from datetime import datetime
from math import ceil


def read_phone_info(csv_name):

    with open(csv_name, 'r') as phone_info:
        reader = csv.reader(phone_info)
        read_phone_info = [row for row in reader]
    return read_phone_info


data_phonetime = read_phone_info('payphonehero_data_phonetime.csv')
data_herocategory = read_phone_info('payphonehero_data_herocategory.csv')
data_salary = read_phone_info('payphonehero_data_salary.csv')

def time_convert(phonetime):

    data_time_list = []

    for i in range(1, len(phonetime) - 1):
        month = datetime.strptime(phonetime[i][1], '%Y-%m-%d %H:%M:%S').strftime('%b %y')
        date = phonetime[i][1].split()[0]
        start = datetime.strptime(phonetime[i][1], '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime(phonetime[i][2], '%Y-%m-%d %H:%M:%S')
        sec = (end - start)
        data_time_list.append([phonetime[i][0], month, date, sec.seconds])
    return data_time_list


def category(hero_category, salary_info):

    category_dict = {hero_category[i][0]: hero_category[i][1] for i in range(1, len(hero_category))}

    call_info_list = time_convert(data_phonetime)

    id_list_with_category = []

    for i in call_info_list:
        id, month, date, seconds = [k for k in i]
        for j in salary_info:
            if id == j[0] and category_dict[month] == j[3]:
                id_list_with_category.append(i)
    return id_list_with_category


def calls_price(calls, salary_info):

    price_list = []

    for i in calls:
        id, month, date, seconds = [k for k in i]
        minutes = ceil(int(seconds) / 60)
        price = 15 * minutes
        price_list.append([id, month, price])

    price_dict = {}

    for i in price_list:
        id, month, price = [k for k in i]
        dict_key = id + ' - ' + month
        price_dict[dict_key] = price_dict.get(dict_key, 0) + price
        for person in range(1, len(salary_info) - 1):
            if id == salary_info[person][0]:
                price_dict[dict_key] = round(price * 100 / int(salary_info[person][4]), 3)
    return price_dict


def pre_hero(call_price):

    salary_percent = {}

    for key, percent in call_price.items():
        id, month = key.split(' - ')
        for key_1, percent_1 in call_price.items():
            id_1, month_1 = key_1.split(' - ')
            if month == month_1:
                if percent > percent_1:
                    salary_percent[month] = id
                else:
                    salary_percent[month] = id_1

    month_list = [data_herocategory[i][0] for i in range(1, len(data_herocategory))]

    for i in month_list:
        if i not in salary_percent:
            salary_percent[i] = None
    return salary_percent


def payphone_hero(winner_dict):

    rus_month = {
        'Jul 99' : "июле 99-го",
        'Aug 99' : "августе 99-го",
        'Sep 99' : "сентябре 99-го",
        'Oct 99' : "октябре 99-го",
        'Nov 99' : "ноябре 99-го",
        'Dec 99' : "декабре 99-го"}

    for month in rus_month:
        if winner_dict[month] == None:
            print(f'Таксофонный герой в {rus_month[month]}: не был определён.')
        for person in range(1, len(data_salary) - 1):
            if winner_dict[month] == data_salary[person][0]:
                print(f'Таксофонный герой в {rus_month[month]}: {data_salary[person][1]} из "{data_salary[person][2]}"')


payphone_hero(pre_hero(calls_price(category(data_herocategory, data_salary), data_salary)))
