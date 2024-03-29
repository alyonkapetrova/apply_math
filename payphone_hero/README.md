# Таксофонный герой

Нырнём в обработку данных! В 2019-ом году выражения "Data Science", "Data Mining", "Machine Learning" произносли с предыханием и священным трепетом. Прикоснёмся же к модному веянию, проанализируем .csv таблицы с помощью чистого python 3.7.

Прямых источников у задачи нет. Немного взяла из [Call to Home](https://py.checkio.org/ru/mission/calls-home/) в Checkio, но условия и входные данные оригинальные.

## Задача

![dse_githubtasks_cover_payphonehero](https://github.com/alyonkapetrova/apply_math/blob/master/payphone_hero/media/dse_githubtasks_cover_payphonehero.svg)

Комитет благополучия Нордии требует от нас отчёта по внедрению программы "Таксофонный герой". Мы, отдел новационных разработок, успешно освоили выделенный бюджет, раструбили всем про нашу программу и должны поделиться своими результатами во благо Нордии. Только у нас ничего не готово.

Наш брат Нордиец - любитель поговорить. Но личных средств связи иметь не положено, поэтому гражданин пользуется **таксофонами** - доступной системой общения всей республики. Люди мало зарабатывают, нуждаются в добром слове от друзей и наша программа делает их жизнь немного проще.

**Таксофонный герой** - программа поддержки рабочего класса, помогает сэкономить на звонках самым нуждающимся Нордийцам. Каждый месяц таксофонным героем **может стать** рабочий определённой профессии, наговоривший больше всего и зарабатывающий меньше всего.

Мы получили всю необходимую информацию: список звонивших от таксофонной компании, данные по работающим и их заработок, условия участия в программе. Но мы не знаем, кто стал таксофонным героем за последние полгода. **Помогите нам узнать** этих счастливчиков.

Шесть героев ждут вашего решения! Спасите репутацию отдела новационных разработок! Не посрамите честь великой Нордии!

* **Проанализируйте данные** и выберите важную для задачи информацию.

* **Разработайте алгоритм** выбора победителя программы по указанным условиям.

* **Узнайте**, кто стал таксофонным героем за указанный период времени.

  > Каждый месяц выбирается свой таксофонный герой. За полгода программа выберет шесть победителей.

## I/O

### Input / Дано:

- Данные для анализа
<br/>**Информация о звонках:** filepayphonehero_data_phonetime.csv;
<br/>**Категории победителей:** payphonehero_data_herocategory.csv;
<br/>**Данные о сотрудниках компаний:** payphonehero_data_salary .csv.

- Тариф
<br/>**Стоимость одной минуты звонка:** 15.

### Output / Найти:

- Имя и место работы таксофонных героев
<br/>**Тип данных:** string.

## Подготовка

В решении задачи используется три модуля для python: csv ([python-документация](https://docs.python.org/3.5/library/csv.html?highlight=csv#module-csv), [csv.reader](https://docs.python.org/3.5/library/csv.html?highlight=csv#module-contents)), datetime ([python-документация](https://docs.python.org/3.5/library/datetime.html?highlight=datetime#module-datetime), [список функций](https://pythonworld.ru/moduli/modul-datetime.html), [datetime.strptime()](https://docs.python.org/3.5/library/datetime.html?highlight=datetime#datetime.datetime.strptime), [datetime.strftime()](https://docs.python.org/3.5/library/datetime.html?highlight=datetime#datetime.datetime.strftime), [форматы даты/времени и флаги](https://docs.python.org/3.5/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior)) и math: ([python-документация](https://docs.python.org/3.5/library/math.html?highlight=math#module-math), [список функций](https://pythonworld.ru/moduli/modul-math.html), [math.ceil](https://docs.python.org/3.5/library/math.html?highlight=math#math.ceil)).

## Решение

__1. Читаем данные__

Данные о звонках, сотрудниках компаний и критериях победителей программы были предоставлены Комитетом в виде csv-таблиц. Перед началом работ, нам нужно их считать.

Используем модуль [csv](https://docs.python.org/3.5/library/csv.html?highlight=csv#module-csv) и его функцию [reader](https://docs.python.org/3.5/library/csv.html?highlight=csv#module-contents).
```
>>> csv_name = 'payphonehero_data_herocategory.csv'
>>> with open(csv_name, 'r') as phone_info:
>>>    reader = csv.reader(phone_info)
>>>    read_phone_info = [row for row in reader]
[['month', 'occupation'], ['Jul 99', 'инженер'], ['Aug 99', 'монтажник'], ['Sep 99', 'специалист'], ['Oct 99', 'сетевик'], ['Nov 99', 'архитектор'], ['Dec 99', 'навигатор']]
```

__2. Преобразовываем данные о звонках__

Исходный файл информации о звонках  __payphonehero_data_phonetime__ содержит данные за последние полгода. Это идентификатор гражданина, данные о времени начала и завершения звонка.

![dse_githubtasks_payphonehero_table_01b](https://github.com/alyonkapetrova/apply_math/blob/master/payphone_hero/media/dse_githubtasks_payphonehero_table_01b.svg)

Посмотрим, что можно с этим сделать.

Данные о времени совершения звонков представлены в формате 'YYYY-MM-DD HH:MM:SS'. Такой формат удобно использовать и преобразовывать с помощью модуля [datetime](https://docs.python.org/3.5/library/datetime.html?highlight=datetime#module-datetime).

Классы [datetime.strptime()](https://docs.python.org/3.5/library/datetime.html?highlight=datetime#datetime.datetime.strptime) и [datetime.strftime()](https://docs.python.org/3.5/library/datetime.html?highlight=datetime#datetime.datetime.strftime) преобразовывают строку в datetime-тип и обратно. Например, из строки '1999-12-04 23:00:20' для переменной month мы получим значение месяца в нужном формате строки 'Dec 99'.

> Подробнее о форматах даты/времени и флагах можно посмотреть [в документации](https://docs.python.org/3.5/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior).

```
>>> month = datetime.strptime(phonetime[i][1], '%Y-%m-%d %H:%M:%S').strftime('%b %y')
Dec 99
```
Из строки начала разговора '1999-12-04 23:00:20' в переменную date записываем значение даты (без времени).
```
>>> date = phonetime[i][1].split()[0]
1999-12-04
```
Переведём даты начала start ('1999-12-04 23:00:20') и окончания end ('1999-12-04 23:04:50') разговора в datetime-тип. Для переменных start и end используем класс [datetime.strptime()](https://docs.python.org/3.5/library/datetime.html?highlight=datetime#datetime.datetime.strptime), а в переменную sec запишем разницу между концом и началом разговора.
```
>>> start = datetime.strptime(phonetime[i][1], '%Y-%m-%d %H:%M:%S')
>>> end = datetime.strptime(phonetime[i][2], '%Y-%m-%d %H:%M:%S')
>>> sec = (end - start)
```
Для дальнейшего анализа, заполним новый список data_time_list следующими данными: идентификатор гражданина, месяц совершения звонка, дата совершения звонка и продолжительность звонка в секундах.
```
>>> data_time_list = []
>>> data_time_list.append([phonetime[i][0], month, date, sec.seconds])
[['55695', 'Dec 99', '1999-12-04', 270], ['45574', 'Oct 99', '1999-10-23', 128], ['37538', 'Dec 99', '1999-12-16', 293], ['95603', 'Aug 99', '1999-08-17', 4882], ['10025', 'Sep 99', '1999-09-23', 102], ['48710', 'Oct 99', '1999-10-20', 95]...]
```

__3. Просеиваем исходные данные__

Создадим словарь из csv-таблицы __payphonehero_data_herocategory__. В нём будут храниться категории победителя программы для каждого месяца за последние полгода.

![dse_githubtasks_payphonehero_table_01c](https://github.com/alyonkapetrova/apply_math/blob/master/payphone_hero/media/dse_githubtasks_payphonehero_table_01c.svg)
```
>>> category_dict = {hero_category[i][0]: hero_category[i][1] for i in range(1, len(hero_category))}
{'Jul 99': 'инженер', 'Aug 99': 'монтажник', 'Sep 99': 'специалист', 'Oct 99': 'сетевик', 'Nov 99': 'архитектор', 'Dec 99': 'навигатор'}
```
Теперь мы знаем, как определить таксофонного героя в любой из последних шести месяцев. Идём дальше и отсеим ненужные данные из списка совершённых звонков, полученого на предыдущем шаге.

Запишем в переменную call_info_list список данных о совершённых звонках. Создадим пустой список id_list_with_category, в котором будут храниться просеянные данные.
```
>>> call_info_list = time_convert(data_phonetime)
>>> id_list_with_category = []
[['55695', 'Dec 99', '1999-12-04', 270], ['45574', 'Oct 99', '1999-10-23', 128], ['37538', 'Dec 99', '1999-12-16', 293], ['95603', 'Aug 99', '1999-08-17', 4882], ['10025', 'Sep 99', '1999-09-23', 102], ['48710', 'Oct 99', '1999-10-20', 95]...]
```
Чтобы узнать, может ли гражданин Нордии стать таксофонным героем, нам понадобится информация о сотрудниках компаний и занимаемых должностях из таблицы __payphonehero_data_salary__.

![dse_githubtasks_payphonehero_table_01a](https://github.com/alyonkapetrova/apply_math/blob/master/payphone_hero/media/dse_githubtasks_payphonehero_table_01a.svg)

Для использования данных таблицы нам понадобится список salary_info.
```
>>> salary_info = data_salary = read_phone_info('payphonehero_data_salary.csv')
[['id', 'name', 'company', 'occupation', 'salary'], ['10025', 'Захар Краави', 'Промсервис 101', 'инженер', '2540'], ['29682', 'Одра Белякова', 'Старейший Йоп ЛТД', 'системщик', '4100'], ['37538', 'Ася Вейер-Круглова', 'Кожевенный3000', 'корпорат', '780'], ['29990', 'Мирон Демидов', 'Общелокальная Омега', 'сетевик', '1600']...]
```
Алгоритм проверки работает так:
1. Из списка call_info_list для сравнения берутся значения идентификатора гражданина и месяца совершения звонка.

2. В списке salary_info ищется запись по идентификатору звонившего гражданина.

3. Проверяется соответствие должности гражданина подходящей должности из category_dict.

Если сотрудник соответствует критерию, запись с информацией о совершённом им звонке переносится из списка call_info_list в новый список id_list_with_category.
```
>>> id_list_with_category = []
>>> for i in call_info_list:
>>>   id, month, date, seconds = [k for k in i]
>>>   for j in salary_info:
>>>     if id == j[0] and category_dict[month] == j[3]:
>>>       id_list_with_category.append(i)
[['97166', 'Oct 99', '1999-10-07', 402], ['92337', 'Aug 99', '1999-08-08', 199], ['37680', 'Jul 99', '1999-07-24', 186], ['97166', 'Oct 99', '1999-10-11', 67], ['73488', 'Oct 99', '1999-10-21', 364], ['85292', 'Sep 99', '1999-09-22', 267], ['98310', 'Sep 99', '1999-09-08', 1986], ['97166', 'Oct 99', '1999-10-02', 77], ['49469', 'Dec 99', '1999-12-07', 1085]]
```
![dse_githubtasks_payphonehero_table_02a](https://github.com/alyonkapetrova/apply_math/blob/master/payphone_hero/media/dse_githubtasks_payphonehero_table_02a.svg)

Ещё на шаг ближе к цели!

__4. Считаем стоимость звонков__

Каждая минута разговора в таксофонах Нордии обходится в 15 кредитов. Переводим длительность каждого разговора в минуты (не забываем округлить в большую сторону).

> Длительность таксофонного разговора округляется в пользу владельца таксофона (да здравствует Нордия!). Например, если звонок длился 61 секунду, необходимо оплатить 2 минуты.

Для округления в большую сторону используем модуль [math](https://docs.python.org/3.5/library/math.html?highlight=math#module-math) и его функцию [ceil](https://docs.python.org/3.5/library/math.html?highlight=math#math.ceil).

Количество минут умножаем на 15 и записываем в переменную price.
```
>>> seconds = 402
>>> minutes = ceil(int(seconds) / 60)
>>> price = 15 * minutes
7
105
```
После подсчётов в список price_list записываем идентификатор гражданина, месяц совершения звонка и его стоимость.
```
>>> price_list.append([id, month, price])
['97166', 'Oct 99', 105]
```
Каждый месяц на таксофонного героя могут претендовать сразу несколько граждан Нордии. По правилам программы, победителем становится нордиец, отдавший за звонки большую часть своего ежемесячного заработка.

Перед окончательным подсчётом объединим звонки гражданина (если за месяц их было больше одного). Словарь price_dict хранит данные о стоимости всех звонков гражданина за месяц. Для записи в словаре нужен уникальный ключ, состоящий из идентификатора гражданина и месяца совершения звонка.
```
>>> dict_key = id + ' - ' + month
97166 - Oct 99
```
Так, стоимость всех звонков каждого нордийца будет подсчитана в одной записи словаря.
```
>>> price_dict[dict_key] = price_dict.get(dict_key, 0) + price
165
```
Определим ушедшую на оплату звонков долю зарплаты граждан. По идентификатору гражданина находим его оклад в таблице __payphonehero_data_salary__. Значение доли округлим до трёх знаков после запятой, чтобы увеличить точность. В соответствующей записи в словаре заменим значение на долю от зарплаты.
```
>>> price_dict[dict_key] = round(price * 100 / int(salary_info[person][4]), 3)
0.75
```

__5. Выявляем таксофонного героя__

В словаре price_dict всё ещё есть несколько претендентов на победу в программе. Зная долю от заработной платы за звонки каждого из них, мы можем выбрать таксофонного героя. Внесём в словарь salary_percent граждан с максимальным значением доли от зарплаты за каждый месяц программы. Ключ словаря - месяц звонка, а значение - идентификатор гражданина.
```
>>> if month == month_1:
>>>   if percent > percent_1:
>>>     salary_percent[month] = id
>>>   else:
>>>     salary_percent[month] = id_1
Oct 99: 73488
```
Перед объявлением победителей программы убедимся, что отчёт для Комитета благополучия Нордии будет полным. Проверим, все ли отчётные месяцы указаны в salary_percent. Используем список отчётных месяцев из таблицы __payphonehero_data_herocategory__.
```
>>> month_list = [data_herocategory[i][0] for i in range(1, len(data_herocategory))]
['Jul 99', 'Aug 99', 'Sep 99', 'Oct 99', 'Nov 99', 'Dec 99']
```
Сравниваем значения ключей из salary_percent с элементами из month_list. Если в словаре не хватает какого-то месяца, записываем его в salary_percent со значением None.
```
>>> for i in month_list:
>>>   if i not in salary_percent:
>>>     salary_percent[i] = None
Nov 99: None
```

__6. Выводим результаты__

В цикле из словаря rus_month (словарь с русскими названиями месяцев) берём ключи (month) и проверяем наличие победителя в итоговом словаре winner_dict. Если победителя в этом месяце не оказалось, выводим сообщение.
```
>>> if winner_dict[month] == None:
>>>   print(f'Таксофонный герой в {rus_month[month]}: не был определён.')
Таксофонный герой в ноябре 99-го: не был определён.
```
Если же победитель определён, находим его имя и место работы в  __payphonehero_data_salary__ по идентификатору гражданина. Объявляем Нордии таксофонного героя.
```
>>> if winner_dict[month] == data_salary[person][0]:
>>>   print(f'Таксофонный герой в {rus_month[month]}: {data_salary[person][1]} из "{data_salary[person][2]}"')
Таксофонный герой в июле 99-го: Кая Васильева из "Яогаи Автоматик"
```
Мы справились с задачей. Das Ist Wunderbar!
