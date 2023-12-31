
import numpy as np
import pandas as pd

if __name__ == '__main__':
    # Создать строки
    date_strings = np.array(['03-04-2005 11:35 PM',
                             '23-05-2010 12:01 AM',
                             '04-09-2009 09:09 PM'])

    # Конвертировать в метки datetime
    X = [pd.to_datetime(date, format='%d-%m-%Y %I:%M %p') for date in date_strings]
    print(X)