# -*- coding: utf-8 -*-

from math import sqrt


dogs_places = input("Enter the dogs's coordinates (ex.: 0,4; 6,12; 10,14): ")
coordinates_list = [tuple(map(float, i.split(','))) for i in dogs_places.split('; ')]


def wild_dogs(coords):

    distance_list = []
    count_list = []

    for point_1 in coords: # выбор первой точки прямой
        for point_2 in coords: # выбор второй точки прямой
            if point_1 != point_2:
                a = point_1[1] - point_2[1] # вычисление коэффициэнта a
                b = point_2[0] - point_1[0] # вычисление коэффициэнта b
                c = point_1[0] * point_2[1] - point_2[0] * point_1[1] # вычисление коэффициэнта c

                distance = round((abs(c) / sqrt(a ** 2 + b ** 2)), 2) # расстояние от точки (0,0) до выбранной прямой на плоскости

                count = sum(1 for point in coords if a * point[0] + b * point[1] + c == 0) # подсчёт количества точек, лежащих на проверяемой прямой

                distance_list.append([count, distance]) # запись пары [кол-во точек на проверяемой прямой / расстояние до прямой от точки (0,0)]
                count_list.append(count) # запись кол-ва точек, лежащих на проверяемой прямой

    answer = sorted([i for i in distance_list if i[0] == max(count_list)]) #  отсортированный по возрастанию список пар (count, distance) с максимальным значением count

    return answer[0][1] # т.к. все значения count в списке answer одинаковы, сортировка происходит по значению distance. Значит минимальное рсстояние до (0,0) при максимальном количестве точек на прямой будет первым элементом списка answer
