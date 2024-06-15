from typing import Any
import logging

games_file: str = './data/vgchartz-2024.csv'
games_header_file: str = './data/vg_data_dictionary.csv'

def process_file(file_to_read: str, mode:str = 'r') -> list[str] | dict[str, Any]:
    with open(file=file_to_read, mode=mode) as file:
        return file.read()

def logger(level: str) -> None:
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')