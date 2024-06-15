from data.data import read_games_data
from globals.globals import games_file
from pandas import DataFrame
from typing import Any
import pandas as pd



def extract() -> DataFrame:
    data: DataFrame = read_games_data(games_file)
    return data

def transform(games_df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform the games DataFrame by filtering, cleaning, and converting data types.
    Parameters:
    games_df (pd.DataFrame): The input DataFrame to be transformed.
    Returns:
    pd.DataFrame: The transformed DataFrame.
    """
    if games_df.empty:
        return pd.DataFrame()

    # Drop rows with missing values
    games_df = games_df.dropna(axis=0, how='any')

    games_df = games_df.drop_duplicates()

    # Filter rows based on console, genre, total sales, and critic score
    games_df = games_df[
        (games_df['console'].str.strip().isin(['PS3', 'PS4', 'X360', 'XOne', 'PC'])) | 
        (games_df['genre'].str.strip().isin(['Shooter', 'Action-Adventure', 'Sports', 'Action', 'Racing', 'Fighting', 'Puzzle', 'Role-Playing', 'Simulation', 'Adventure', 'Misc', 
                                                'Strategy'])) |  (games_df['total_sales'].ge(5)) | (games_df['critic_score'].ge(6))
    ].reset_index(drop=True)

    # Define columns to convert and their corresponding data types
    columns_to_convert: dict[str, Any] = {
        'img': str, 'title': str, 'console': str, 'genre': str, 
        'publisher': str, 'developer': str, 'critic_score': float, 
        'total_sales': float, 'na_sales': float, 'jp_sales': float, 
        'pal_sales': float, 'other_sales': float
    }

    # Convert columns to their corresponding data types
    for col, col_type in columns_to_convert.items():
        if col in games_df.columns:
            games_df[col] = games_df[col].astype(col_type)

    # Define date columns to convert to datetime
    date_columns: list[str] = ['release_date', 'last_update']

    # Convert date columns to datetime
    for date_col in date_columns:
        if date_col in games_df.columns:
            games_df[date_col] = pd.to_datetime(games_df[date_col])

    return games_df

data = extract()
trans = transform(data)
print(trans['console'])