from random import randint

a = input("Введите объём машин и максимальную длину бревна: ")

def forest_generator():

    capacity, max_len = [int(i) for i in a.split()]

    sum_truck = capacity
    truck = []
    k = 0
    while sum_truck > max_len:
        trunk = [randint(0,1) for i in range(randint(2, max_len))]
        truck.append(trunk)
        sum_truck -= len(truck[k])
        k += 1
    truck.append([randint(0,1) for i in range(sum_truck)])
    return truck


forest_1 = forest_generator()
forest_2 = forest_generator()


def forest_cut(truck):

    cut = 0
    profit = 0

    for trunk in truck:
        for i in range(0, len(trunk)):
            if trunk[i] == 1:
                if i == len(trunk) - 1 and trunk[i - 1] == 1:
                    profit += 200
                elif i == 0 or i == len(trunk) - 1:
                    cut += 50
                    profit += 200
                elif trunk[i - 1] == 0 and trunk[i + 1] == 0 or trunk[i - 1] == 0 and trunk[i + 1] == 1:
                    cut += 100
                    profit += 200
                else:
                    cut += 50
                    profit += 200

    total = profit - cut
    return total


def best_price(cut_1, cut_2):

    if cut_1 > cut_2:
        print(f"Первый грузовик принесёт {cut_1} кредитов (на {cut_1 - cut_2} кредитов больше, чем второй ({cut_2})).")
    else:
        print(f"Второй грузовик принесёт {cut_2} кредитов (на {cut_2 - cut_1} кредитов больше, чем первый ({cut_1})).")



best_price(forest_cut(forest_1), forest_cut(forest_2))
