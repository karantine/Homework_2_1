def get_dict(filename):
    cook_book = {}
    line_number = 0
    cur_key = ''
    with open(filename, encoding='utf8') as f:
        for line in f:
            stripped_line = line.strip()
            if len(stripped_line) == 0:
                line_number = 0
                continue
            line_number = line_number + 1
            if line_number == 1:
                cook_book[stripped_line] = []
                cur_key = stripped_line
            elif line_number > 2:
                ingredient = line.split('|')
                dish_ing = {}
                dish_ing['ingredient_name'] = ingredient[0]
                dish_ing['quantity'] = ingredient[1]
                dish_ing['measure'] = ingredient[2]
                cook_book[cur_key].append(dish_ing)
    return cook_book


def get_shop_list(dishes, person_count):
    cook_book = get_dict('recipes.txt')
    shop_list_local = {}
    for dish_item in dishes:
        ingredients = cook_book[dish_item]
        for ingredient in ingredients:
            name = ingredient['ingredient_name']
            if name in shop_list_local:
                temp = shop_list_local[name]
                temp['quantity'] = int(temp['quantity']) + int(ingredient['quantity']) * person_count
            else:
                temp_dict = {}
                temp_dict['measure'] = ingredient['measure']
                temp_dict['quantity'] = int(ingredient['quantity']) * person_count
                shop_list_local[name] = temp_dict
    return shop_list_local


shop_list = get_shop_list(['Омлет', 'Фахитос'], 2)

print('Требуемые ингредиенты:\n{}\n'.format(shop_list))
