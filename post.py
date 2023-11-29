towns = [
  {
    'name': "Kyiv",
    'coord': [50.234, 35.12],
  },
  {
    'name': "Lviv",
    'coord': [43.234, 33.12],
  },
  {
    'name': "Odessa",
    'coord': [46.234, 21.12],
  },
]

price = 5

def Post (city1, city2, weight):

    coord1, coord2 = None, None
    

    for town in towns:
        if city1 == town['name']:
            coord1 = town['coord']
        if city2 == town['name']:
            coord2 = town['coord']

    result = ((coord1[0] - coord2[0]) + (coord1[1] - coord2[1])) * price

    return round(result * weight)


print(Post("Kyiv", "Odessa", 2))