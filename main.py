from etl.etl import extract, transform, load, log_process
from globals.globals import LOGGING_INFO, LOGGING_INFO_FUNCTION
from pandas import DataFrame


def main_logger(
    message: str,
    level=LOGGING_INFO,
    log_function=LOGGING_INFO_FUNCTION
) -> None:
    log_process(message=message, level=level, log_function=log_function)


def main() -> None:
    main_logger('Starting Process!!!')

    # Extraction
    main_logger('Starting Extraction Process!!!')
    extract_data: DataFrame = extract()
    main_logger('Ending Extraction Process!!!')

    # Transformation
    main_logger('Starting Transforming Process!!!')
    transform_data: DataFrame = transform(extract_data)
    main_logger('Ending Transforming Process!!!')

    # Loading
    main_logger('Starting Loading Process!!!')
    load(transform_data)
    main_logger('Ending Loading Process!!!')

    main_logger('Ending Process!!!')


# Execute the main function
if __name__ == '__main__':
    main()
