
import pandas as pd
import matplotlib.pyplot as plt

# https://github.com/microsoft/ML-For-Beginners/blob/main/2-Regression/2-Data/README.md

# Use the head() function to view the first five rows.
def get_head(output: bool = False):
    pumpkins = pd.read_csv('data/US-pumpkins.csv')
    pumpkins = pumpkins[pumpkins['Package'].str.contains('bushel', case=True, regex=True)]
    head = pumpkins.head()
    if output:
        print(head)
    return head


def get_selected_columns(output: bool = False):
    pumpkins_head = get_head()
    columns = ['Package', 'Low Price', 'High Price', 'Date']
    pkg_price_hprice_data = pumpkins_head.loc[:, columns]
    if output:
        print(pkg_price_hprice_data)
    return pkg_price_hprice_data


if __name__ == '__main__':

    # print_head(False)
    # get_selected_columns(False)

    # print_head(True)
    pumpkins = get_selected_columns(True)

    # Get an average between low and high price for the base pumpkin price
    price = (pumpkins['Low Price'] + pumpkins['High Price']) / 2

    # Convert the date to its month only
    month = pd.DatetimeIndex(pumpkins['Date']).month

    # Create a new dataframe with this basic data
    new_pumpkins = pd.DataFrame({'Month': month, 'Package': pumpkins['Package'], 'Low Price': pumpkins['Low Price'],'High Price': pumpkins['High Price'], 'Price': price})

    # Convert the price if the Package contains fractional bushel values
    new_pumpkins.loc[new_pumpkins['Package'].str.contains('1 1/9'), 'Price'] = price/(1 + 1/9)
    new_pumpkins.loc[new_pumpkins['Package'].str.contains('1/2'), 'Price'] = price/(1/2)

    # print(new_pumpkins)

    price = new_pumpkins.Price
    month = new_pumpkins.Month
    plt.scatter(price, month)
    plt.show()

    new_pumpkins.groupby(['Month'])['Price'].mean().plot(kind='bar')
    plt.ylabel("Pumpkin Price")