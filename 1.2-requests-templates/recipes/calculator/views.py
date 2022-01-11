from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'salat': {
        'Белокочанная капуста, г.': 300,
        'Морковь, шт.': 1,
        'Луковица, шт.': 1,
        'Чеснок, зубчиков': 3,
        'Подсолнечное масло, ст. ложек': 3,
        'Уксус, ч. ложек': 1,
        'Сахар, ч. ложек': 2,
        'Соль': 'по вкусу'
    }
}


def recipe_name(request, bludo):
    amount_multiply = float(request.GET.get('servings', 1))
    recipe_data = {bludo: {}}
    for ingredient, amount in DATA[bludo].items():
        if isinstance(amount, int) is True:
            recipe_data[bludo].update({ingredient: int(amount * amount_multiply)})
        elif isinstance(amount, str) is True:
            recipe_data[bludo].update({ingredient: amount})
        else:
            recipe_data[bludo].update({ingredient: round(amount * amount_multiply, 3)})
    context = {
        'recipe': recipe_data[bludo],
        'bludo': bludo
    }
    return render(request, 'calculator/index.html', context)

