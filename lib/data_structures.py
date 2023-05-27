spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(foods):
    return [food["name"] for food in foods]

def get_spiciest_foods(foods):
    return [food for food in foods if food["heat_level"] > 5]

def print_spicy_foods(foods):
    for food in foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_spicy_food_by_cuisine(foods, cuisine):
    for food in foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(foods):
    spiciest_foods = get_spiciest_foods(foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(foods):
    heat_levels = [food["heat_level"] for food in foods]
    return sum(heat_levels) / len(heat_levels)

def create_spicy_food(foods, new_food):
    return foods + [new_food]
