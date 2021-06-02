# Как можно это использовать? Давайте наполним список остатками от деления числа на значение счётчика.
flowers = {
    "iris_setosa": {
        "sepal_length": [3.6, 4.9, 4.8, 4.7],
        "sepal_width": [2.9, 3.3, 3.2, 3.1],
        "petal_length": [1.3, 1.2, 1.5, 1.4],
    },
    "iris_virginica": {
        "sepal_length": [7.2, 7.0, 7.9],
        "sepal_width": [3.1, 2.7, 2.8],
        "petal_length": [5.5, 5.5, 6.5],
    },
    "iris_versicolor": {
        "sepal_length": [6.5, 6.0, 6.1, 6.2, 6.3],
        "sepal_width": [2.8, 2.9, 2.4, 2.7, 2.7],
        "petal_length": [4.8, 4.7, 5.0, 4.9, 4.8],
    },
}

x = []
y = []
z = []
s = [[x, y] for x, y in flowers.items()]
for key, val in flowers.items():
    x.extend(val['sepal_length']), y.extend(val['sepal_width']), z.extend(val['petal_length'])


print('mid sepal_length= {0}\nmid sepal_width= {1}\nmid petal_length= {2}'.format(sum(x) / len(x),
                                                                                  sum(y) / len(y),
                                                                                  sum(z) / len(z)))
