import pandas as pd


def display():
    dataFrame = pd.read_csv('Pandas\\pokemon_data.csv')

    print(dataFrame.head(5))

