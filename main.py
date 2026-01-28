"""
Задача №1
"""

import os


def get_dict_cook_book(str_):
    '''
    
    converts a string recipe
        Омлет
        3
        Яйцо | 2 | шт
        Молоко | 100 | мл
        Помидор | 2 | шт
    to dict
        {'Омлет': [
            {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
            {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
            {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
            ]
        }
    :param str_:
    :return a dictionary:
    '''
    result_dict = {}
    array_str = str_.split('\n')
    list_keys = ['ingredient_name', 'quantity', 'measure']

    for i, value in enumerate(array_str):
        if not value:
            continue
        if i == 0:
            list_ = result_dict.setdefault(array_str[0], [])
        else:
            list_value = list(map(lambda s: s.strip(), value.split('|')))
            list_value[1] = int(list_value[1]) if list_value[1].isdigit() else 0
            d = dict(zip(list_keys, list_value))
            list_.append(d)
    return result_dict


def show_cook_book(dict_):
    print('cook_book = {')
    if dict_:
        for key, value in dict_.items():
            print(f" '{key}': [", ",\n   ".join(str(item) for item in value) + "\n   ],", sep="\n   ")
    print(' }')


def read_file_recipes_book():
    '''

    reading recipes from a file
    :return the recipe book as a dictionary
            example
            cook_book = {
                  'Омлет': [
                    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
                    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
                    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
                    ],
                  'Утка по-пекински': [
                    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
                    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
                    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
                    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
                    ],
                  'Запеченный картофель': [
                    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
                    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
                    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
                    ]
                  }:
    '''
    path = os.path.join("resources", "cookBook", "recipes.txt")
    cook_book = {}
    if os.path.exists(path):
        with open(path, encoding='utf-8') as file:
            s = ""
            count_line_recipe = 0
            count_ = 0
            for line_file in file:
                if line_file.strip() == "":
                    continue
                if count_ == 0 or count_ < count_line_recipe:
                    s += line_file
                    count_ += 1
                elif count_ == 1 and line_file.strip().isdigit():
                    count_line_recipe = int(line_file)
                else:
                    s += line_file
                    cook_book.update(get_dict_cook_book(s))
                    s = ""
                    count_line_recipe = 0
                    count_ = 0
    return cook_book


show_cook_book(read_file_recipes_book())
