class Restaurant:
    name = ''
    category = ''
    rating = 0.0
    delivery = False


class Restaurant1:
    name = ''
    category = ''
    rating = 0.0
    delivery = False


class Restaurant2:
    name = ''
    category = ''
    rating = 0.0
    delivery = False


bobs = Restaurant

bobs.name = 'Bobs\'s Burgers'
bobs.category = 'American Diner'
bobs.rating = 4.7
bobs.delivery = False

waffle_house = Restaurant1

waffle_house.name = 'Waffle House'
waffle_house.category = 'Breakfast Diner'
waffle_house.rating = 4.3
waffle_house.delivery = False

mcd = Restaurant2

mcd.name = 'McDonald\'s'
mcd.category = 'Fast Food'
mcd.rating = 4.1
mcd.delivery = False

print(vars(bobs))

print(vars(waffle_house))

print(vars(mcd))
