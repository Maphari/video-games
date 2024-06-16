from pandas import DataFrame
from data.data import read_games_data
from globals.globals import (
    games_file, LOGGING_ERROR_FUNCTION, LOGGING_ERROR, LOGGING_INFO_FUNCTION,
    LOGGING_INFO, log_process
)
from typing import Any, Optional
from dotenv import load_dotenv
from sqlalchemy import create_engine  # commented out (text) function
from sqlalchemy.engine import Engine, Connection
import pandas as pd
import os

load_dotenv()


def extract() -> DataFrame:
    data: DataFrame = read_games_data(games_file)
    return data


def transform(games_df: pd.DataFrame) -> pd.DataFrame:
    if games_df.empty:
        return pd.DataFrame()

    # Drop duplicates
    games_df = games_df.drop_duplicates()
    # Drop rows with missing values
    games_df = games_df.dropna(axis=0, how='any')
    # Filter rows based on console, genre, total sales, and critic score
    games_df = games_df[
        (games_df['genre'].str.strip().isin([
            'Shooter', 'Action-Adventure', 'Sports', 'Action', 'Racing',
            'Fighting', 'Puzzle', 'Role-Playing', 'Simulation', 'Adventure',
            'Misc', 'Strategy'
        ])) &
        (games_df['console'].str.strip().isin([
            'PS3', 'PS4', 'X360', 'XOne', 'PC'
        ])) &
        (games_df['total_sales'] > 0) &
        (games_df['critic_score'] > 0)
    ]
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

    return games_df.reset_index(drop=True)


def load(game_df: DataFrame) -> None:
    if game_df.empty:
        return pd.DataFrame()

    table_name: str = os.getenv('TABLE_NAME')
    connection_string: str = (
        f"mssql+pyodbc://{os.getenv('USERNAME')}:{os.getenv('PASSWORD')}"
        f"@{os.getenv('SERVER')}/{os.getenv('DATABASE')}?driver=ODBC"
        f"+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
    )

    conn: Optional[Connection] = None
    try:
        engine: Engine = create_engine(connection_string)
        log_process("Connection to SQL Server established successfully.",
                    level=LOGGING_INFO, log_function=LOGGING_INFO_FUNCTION)
    except Exception as e:
        log_process(f'Unexpected exception {e}', level=LOGGING_ERROR,
                    log_function=LOGGING_ERROR_FUNCTION)
    else:
        # Write the DataFrame to SQL Server
        game_df.to_sql(
            table_name, con=engine, if_exists='replace', index=False
        )
        log_process(f"DataFrame written to table {table_name} successfully.",
                    level=LOGGING_INFO, log_function=LOGGING_INFO_FUNCTION)

        # with engine.connect() as connection:
        #     result = connection.execute(
        #         text(f"SELECT TOP 2 * FROM {table_name}")
        #     )
        #     for row in result:
        #         print(row)
    finally:
        if conn is not None:
            conn.close()
