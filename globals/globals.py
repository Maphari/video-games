from typing import Any, Union
import logging
import os


games_file: str = './data/vgchartz-2024.csv'
games_header_file: str = './data/vg_data_dictionary.csv'

LOGGING_ERROR = logging.ERROR
LOGGING_ERROR_FUNCTION = logging.error
LOGGING_INFO = logging.INFO
LOGGING_INFO_FUNCTION = logging.info


def process_file(
    file_to_read: str,
    mode: str = 'r'
) -> Union[list[str] | dict[str, Any]]:
    with open(file=file_to_read, mode=mode) as file:
        return file.read()


def logger(level: str) -> None:
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def log_process(message: str, level: str, log_function) -> None:
    log_directory: str = 'logs'
    logs_file: str = 'process_logs.log'
    logs_path: str = os.path.join(log_directory, logs_file)

    if not os.path.exists(logs_path):
        os.mkdir(log_directory)

    logging.basicConfig(
        filename=logs_path,
        level=level,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    log_function(f'{message}')
