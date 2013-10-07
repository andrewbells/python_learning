fruit_to_color = {'banana' : 'yellow', 'cherry' : 'red', 'pear' : 'green', 'apple': 'yellow'}

color_to_fruit = {}
for fruit in fruit_to_color:
    color = fruit_to_color[fruit]
    if not (color in color_to_fruit):
        color_to_fruit[color] = [fruit]
    else:
        color_to_fruit[color].append(fruit)
    
