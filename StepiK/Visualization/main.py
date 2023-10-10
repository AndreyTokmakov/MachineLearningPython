from collections import defaultdict

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns

DATA_FILE = "../data/ataset_209770_6.txt"
GENOME_DATA = "../data/genome_matrix.csv"
DOTA_DATASET = "../data/dota_hero_stats.csv"
IRIS = "../data/iris.csv"

if __name__ == '__main__':
    # data = pd.read_csv(DATA_FILE, sep=' ')
    iris_data = pd.read_csv(IRIS)

    print(iris_data)

    # plt.show()
