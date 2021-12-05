from django.shortcuts import render, reverse

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
    # можете добавить свои рецепты ;)
}


def omlet(request):
    count_p = int(request.GET.get('servings', 1))
    DATA = {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5
    }
    context = {'recipe': dict(map((lambda x: (x, float(DATA[x]) * count_p)), DATA.keys()))}

    return render(request, 'calculator/index.html', context)


def pasta(request):
    count_p = int(request.GET.get('servings', 1))
    DATA = {
        'макароны, г': 0.3,
        'сыр, г': 0.05
    }
    context = {'recipe': dict(map((lambda x: (x, float(DATA[x]) * count_p)), DATA.keys()))}

    return render(request, 'calculator/index.html', context)


def buter(request):
    count_p = int(request.GET.get('servings', 1))
    DATA = {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1
    }
    context = {'recipe': dict(map((lambda x: (x, float(DATA[x]) * count_p)), DATA.keys()))}

    return render(request, 'calculator/index.html', context)


def index(request):
    return render(request, 'calculator/index.html')
