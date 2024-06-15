import logging
import pandas as pd
from pandas import DataFrame
from globals.globals import logger

logger(logging.ERROR)

def read_games_data(file_to_process: str) -> DataFrame:
    try:
        games_df: DataFrame = pd.read_csv(file_to_process)
    except FileNotFoundError as e:
        logging.error(f'File not found: {e}')
    except pd.errors.EmptyDataError as e:
        logging.error(f'File is empty: {e}')
    except pd.errors.ParserError as e:
        logging.error(f'File could not be parsed: {e}')
    except Exception as e:
        logging.error(f'Unexpected exception {e}', exc_info=True)
    else:
        return games_df

    return pd.DataFrame()
