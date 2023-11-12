from sklearn import datasets


if __name__ == '__main__':
    # Загрузить набор изображений рукописных цифр
    digits = datasets.load_digits()

    # Создать матрицу признаков
    features = digits.data

    # Создать вектор целей
    target = digits.target

    print(target)

    # Взглянуть на первое наблюдение
    print(features[0])
