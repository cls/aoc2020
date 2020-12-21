import re
import sys

pattern = re.compile(r'(.*) \(contains (.*)\)')

foods = []
allergen_to_ingredients = {}

for line in sys.stdin:
    match = pattern.match(line)
    ingredients_s, allergens_s = match.group(1, 2)
    ingredients = ingredients_s.split(' ')
    allergens = allergens_s.split(', ')
    foods.append(ingredients)
    for allergen in allergens:
        if allergen in allergen_to_ingredients:
            allergen_to_ingredients[allergen] &= set(ingredients)
        else:
            allergen_to_ingredients[allergen] = set(ingredients)

ingredient_to_allergens = {}

for allergen, ingredients in allergen_to_ingredients.items():
    for ingredient in ingredients:
        ingredient_to_allergens.setdefault(ingredient, set()).add(allergen)

count = 0

for food in foods:
    for ingredient in food:
        if ingredient not in ingredient_to_allergens:
            count += 1

print(count)

def resolve_conflicts():
    for allergen, ingredients in allergen_to_ingredients.items():
        if len(ingredients) == 1:
            ingredient = next(iter(ingredients))
            for other_allergen, other_ingredients in allergen_to_ingredients.items():
                if allergen != other_allergen and ingredient in other_ingredients:
                    other_ingredients.remove(ingredient)
                    return True
    return False

while resolve_conflicts():
    pass

dangerous_ingredients = []

for allergen, ingredients in sorted(allergen_to_ingredients.items()):
    if len(ingredients) != 1:
        raise Exception("Expected unique allergenic")
    dangerous_ingredients.extend(ingredients)

print(','.join(dangerous_ingredients))
