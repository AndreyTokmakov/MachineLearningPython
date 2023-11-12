
import pandas as pd


def load_csv():
    # Загрузить набор данных
    dataframe = pd.read_csv('/home/andtokm/DiskS/ProjectsUbuntu/MachineLearningPython/Pandas/data/anime.csv')

    # Взглянуть на первые две строки
    print(dataframe.head())


if __name__ == '__main__':
    load_csv()

