def get_dict(filename):
  cook_book = {}
  line_number = 0
  cur_key = ''
  with open(filename, encoding='utf8') as f:
    for line in f:
      l = line.strip()
      if len(l) == 0: 
        line_number = 0 
        continue
      line_number = line_number + 1
      if line_number == 1: 
        cook_book[l] = []
        cur_key = l      
      elif line_number > 2:
        ingredient = line.split('|')
        d = {}
        d['ingredient_name'] = ingredient[0]
        d['quantity'] = ingredient[1]
        d['measure'] = ingredient[2]
        cook_book[cur_key].append(d)
  return cook_book

cook_book_dict = get_dict('recipes.txt')
print('Словарь с блюдами:\n{}\n'.format(cook_book_dict))
        
def get_shop_list(cook_book, dishes, person_count):
  shop_list = {}
  for d in dishes:
    ingredients = cook_book[d]
    for ingredient in ingredients:
      name = ingredient['ingredient_name']
      if name in shop_list:
        temp = shop_list[name]
        temp['quantity'] = int(temp['quantity']) + int(ingredient['quantity']) * person_count
      else:
        temp_dict = {}
        temp_dict['measure'] = ingredient['measure']
        temp_dict['quantity'] = int(ingredient['quantity']) * person_count
        shop_list[name] = temp_dict 
  return shop_list
 
shop_list = get_shop_list(cook_book_dict, ['Омлет', 'Фахитос'], 2)

print('Требуемые ингредиенты:\n{}\n'.format(shop_list))
