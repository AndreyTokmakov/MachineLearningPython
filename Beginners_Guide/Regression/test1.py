from datetime import datetime

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# https://github.com/microsoft/ML-For-Beginners/blob/main/2-Regression/3-Linear/solution/notebook.ipynb
# https://github.com/microsoft/ML-For-Beginners/blob/main/2-Regression/3-Linear/README.md

if __name__ == '__main__':
    pumpkins = pd.read_csv('data/US-pumpkins.csv')
    pumpkins = pumpkins[pumpkins['Package'].str.contains('bushel', case=True, regex=True)]

    # print('-' * 180, '\n', pumpkins, sep='')

    columns_to_keep = ['Package', 'Variety', 'City Name', 'Month', 'Low Price', 'High Price', 'Date']
    pumpkins = pumpkins.drop([c for c in pumpkins.columns if c not in columns_to_keep], axis=1)

    # print('-' * 180, '\n', pumpkins, sep='')

    price = (pumpkins['Low Price'] + pumpkins['High Price']) / 2
    month = pd.DatetimeIndex(pumpkins['Date']).month
    day_of_year = pd.to_datetime(pumpkins['Date']).apply(lambda dt: (dt - datetime(dt.year, 1, 1)).days)

    new_pumpkins = pd.DataFrame({
        'Month': month,
        'DayOfYear': day_of_year,
        'Variety': pumpkins['Variety'],
        'City': pumpkins['City Name'],
        'Package': pumpkins['Package'],
        'Low Price': pumpkins['Low Price'],
        'High Price': pumpkins['High Price'],
        'Price': price
    })

    new_pumpkins.loc[new_pumpkins['Package'].str.contains('1 1/9'), 'Price'] = price / 1.1
    new_pumpkins.loc[new_pumpkins['Package'].str.contains('1/2'), 'Price'] = price * 2

    new_pumpkins.head()

    '''
    new_pumpkins.plot.scatter('Month', 'Price')
    print(new_pumpkins['Month'].corr(new_pumpkins['Price']))
    plt.ylabel("Month vs Price")
    plt.show()
    '''

    new_pumpkins.plot.scatter('DayOfYear', 'Price')
    # print correlation DayOfYear vs Price --> -0.1667332249274541 -- > BAD
    print(new_pumpkins['DayOfYear'].corr(new_pumpkins['Price']))
    plt.ylabel("DayOfYear vs Price")
    plt.show()
