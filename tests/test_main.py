import polars as pl
from src.main import descriptive_stat, visualize_data

def test_descriptive_stat():
    # Import the DataFrame from the CSV file
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")

    # Calculate summary statistics using the function
    calculated_stats = descriptive_stat(cars)

    # Define expected summary statistics (you can adjust these as needed)
    expected_stats = {
        "summary": ["mean", "stddev"],
        "mpg": [20.38, 6.17],  # Adjust the expected values as needed
        "hp": [119.6, 53.91]   # Adjust the expected values as needed
    }

    # Use assert to compare the calculated stats with the expected stats
    for col in expected_stats["summary"]:
        for column in ["mpg", "hp"]:
            calculated_value = calculated_stats[column].to_pandas().iloc[0]
            expected_value = expected_stats[column][expected_stats["summary"].index(col)]
            assert calculated_value == expected_value

def test_visualize_data():
    # Import the DataFrame from the CSV file
    cars = pl.read_csv(r"https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")

    # Ensure the visualize_data function runs without errors
    visualize_data(cars)

if __name__ == "__main__":
    test_descriptive_stat_mean()
    test_visualize_data()
