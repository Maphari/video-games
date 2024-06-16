import pandas as pd
from pandas import DataFrame
from globals.globals import log_process, LOGGING_ERROR_FUNCTION, LOGGING_ERROR


def read_games_data(file_to_process: str) -> DataFrame:
    try:
        games_df: DataFrame = pd.read_csv(file_to_process)
    except FileNotFoundError as e:
        log_process(f'File not found: {e}', LOGGING_ERROR,
                    LOGGING_ERROR_FUNCTION)
    except pd.errors.EmptyDataError as e:
        log_process(f'File is empty: {e}', LOGGING_ERROR,
                    LOGGING_ERROR_FUNCTION)
    except pd.errors.ParserError as e:
        log_process(f'File could not be parsed: {e}', LOGGING_ERROR,
                    LOGGING_ERROR_FUNCTION)
    except Exception as e:
        log_process(f'Unexpected exception {e}', LOGGING_ERROR,
                    LOGGING_ERROR_FUNCTION)
    else:
        return games_df

    return pd.DataFrame()
