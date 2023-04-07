from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dishes_name = line.strip()
        items_count = int(file.readline().strip())
        dishes = []
        for _ in range(items_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            dishes.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        file.readline()
        cook_book[dishes_name] = dishes

    pprint(cook_book, sort_dicts=False)


def get_shop_list_by_dishes(dish, person):
    """
    :param dish: блюда, которые нужно готовить
    :param person: количество человек
    :return: словарь, ключ: ингридиенты, значение: вложенный словарь с ед.изм. и количеством
    """

    roster = []  # список словарей-ингридиентов для блюд которые надо готовить (из книги рецептов)
    shop_list = {}
    for dish in dish:  # создание списка блюд для готовки
        if dish in cook_book.keys():
            for ingredients in cook_book[dish]:
                roster.append(dict(ingredients))
                shop_list.setdefault((ingredients['ingredient_name']), ({'measure': '', 'quantity': ''}))
        else:
            print(f'Блюда {dish} нет в кулинарной книге')

    for dictionary in roster:
        dictionary['quantity'] *= person

    for dictionary in roster:  # сложение ингридиентов в лист закупок
        i = dictionary['ingredient_name']
        for key in shop_list[i]:
            try:
                shop_list[i][key] += int(dictionary[key])
            except:
                shop_list[i][key] = dictionary[key]

    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
# pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
