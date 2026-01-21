import logging
from pathlib import Path

def setup_logger(name: str, log_config: dict) -> logging.Logger:

    logger = logging.getLogger(name)

    level = getattr(logging , log_config['file_level'].upper(),logging.info)
    logger.setLevel(level)

    if logger.handlers:
        return logger


    formatter = log_config['format']
    log_format = logging.Formatter(formatter)

    file_handler = logging.FileHandler(log_config["path"])
    file_handler.setFormatter(log_format)
    file_handler.setLevel(log_config['file_level'])

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel(log_config['console_level'])

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger



