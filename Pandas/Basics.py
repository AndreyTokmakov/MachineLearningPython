
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1600)

TITANIC_CSV_FILE: str = 'data/titanic.csv'


def create_dataframe():
    dataframe = pd.DataFrame()

    dataframe['Имя'] = ['Джеки Джексон', 'Стивен Стивенсон']
    dataframe['Возраст'] = [38, 25]
    dataframe['Водитель'] = [True, False]

    print(dataframe)


def create_dataframe_add_series():
    dataframe = pd.DataFrame()

    dataframe['Имя'] = ['Джеки Джексон', 'Стивен Стивенсон']
    dataframe['Возраст'] = [38, 25]
    dataframe['Водитель'] = [True, False]

    print(dataframe, '\n')

    new_entry = pd.DataFrame()
    new_entry['Имя'] = ['Молли Муни']
    new_entry['Возраст'] = [40]
    new_entry['Водитель'] = [True]

    dataframe = pd.concat([dataframe, new_entry])

    print(dataframe)


def show_head():
    dataframe = pd.read_csv(TITANIC_CSV_FILE)
    print(dataframe.head(3))


def show_columns():
    dataframe = pd.read_csv(TITANIC_CSV_FILE)
    print(dataframe.columns.values)
    print(dataframe.describe())


def describe():
    dataframe = pd.read_csv(TITANIC_CSV_FILE)
    # получить описательную статстику для любых числовых столбцов
    print(dataframe.describe())


def filter_data():
    dataframe = pd.read_csv(TITANIC_CSV_FILE)

    # Select first 2 rows where 'sex' == 'female'
    females = dataframe[dataframe['Sex'] == 'female'].head(2)
    print(females)

    # Select first 2 rows where 'sex' == 'female' and 'age' >= 60
    females_over_60 = dataframe[(dataframe['Sex'] == 'female') & (dataframe['Age'] >= 60)]
    print(females_over_60.head(2))


def update_values():
    dataframe = pd.read_csv(TITANIC_CSV_FILE)

    # Select first 2 rows where 'sex' == 'female'
    females = dataframe[dataframe['Sex'] == 'female'].head(2)
    print(females)

    result = females['Sex'].replace("female", "Woman").head(2)
    print(result)


def rename_rows():
    dataframe = pd.read_csv(TITANIC_CSV_FILE)

    # Rename column 'Pclass' --> 'Passenger Class'
    result = dataframe.rename(columns={'Pclass': 'Passenger Class'}).head(2)
    print(result)

    print()

    # Rename column 'Pclass' --> 'Passenger Class' and 'Sex' --> 'Gender'
    result = dataframe.rename(columns={'PClass': 'Passenger Class', 'Sex': 'Gender'}).head(2)
    print(result)


if __name__ == '__main__':
    # create_dataframe()
    # create_dataframe_add_series()

    # show_head()
    # show_columns()
    # describe()

    # filter_data()

    # update_values()
    rename_rows()
