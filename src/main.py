import polars as pl
import matplotlib.pyplot as plt

def descriptive_stat(df: pl.DataFrame) -> pl.DataFrame:
    summary_stats = df.describe()
    return summary_stats

def visualize_data(df):
    plt.scatter(df["mpg"], df["hp"])
    plt.xlabel("Miles Per Gallon")
    plt.ylabel("Horse Power")
    plt.title("Miles per gallon changes with automobile weight")
    plt.show()

if __name__ == '__main__':
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
    print(cars.head())
    print(descriptive_stat(cars))
    visualize_data(cars)
