# -*- coding: utf-8 -*-

# выбираем записи для каждого месяца по категории (id-должность-категория победителя)
# считаем стоимость звонков
# вычисляем процент стоимости звонков от зарплаты
# у кого процент больше - тот победитель лотереи (если один участник - он и победитель)

import csv
from datetime import datetime
from math import ceil


def read_phone_info(csv_name):

    with open(csv_name, 'r') as phone_info:
        reader = csv.reader(phone_info)
        read_phone_info = [row for row in reader]
    return read_phone_info


def time_convert():

    a = read_phone_info('payphonehero_data_phonetime.csv')
    b = []

    for i in range(1, len(a) - 1):
        month = datetime.strptime(a[i][1], '%Y-%m-%d %H:%M:%S').strftime('%b %y')
        date = a[i][1].split()[0]
        start = datetime.strptime(a[i][1], '%Y-%m-%d %H:%M:%S')
        end = datetime.strptime(a[i][2], '%Y-%m-%d %H:%M:%S')
        sec = (end - start)
        b.append([a[i][0], month, date, sec.seconds])
    return sorted(b, key=lambda x:x[1])


print(time_convert())


def category():

    a = read_phone_info('payphonehero_data_herocategory.csv')
    b = {a[i][0]: a[i][1] for i in range(1, len(a) - 1)}

    print(b)

category()


def payphone_hero(calls):

    day_dict = {}

    for i in calls:
        date, sec = i[1], i[2]
        minutes = ceil(int(sec) / 60)
        print(date, sec, minutes)
        day_dict[date] = day_dict.get(date, 0) + minutes
    return sum((2 * price - min(price, 100)) for price in day_dict.values())


#print(payphone_hero(time_convert()))
#read_phone_info('payphonehero_data_phonetime.csv')
