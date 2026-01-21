import logging
from pathlib import Path

from  organiser.config_loader import config_loader
from organiser.logger import setup_logger


from organiser.scanner import scan_folder
from organiser.classifier import classifier
from organiser.file_mover import file_mover, FileMoveError


def main() -> None:
    try:

        config = config_loader()
        logger = setup_logger("automated file organiser", config["log_config"])
        source_folder = Path(config["base_path"])
        categories = config['categories']

        logger.info("process started")

        ignored_folders = [source_folder/category for category in categories.keys()]

        for file_path in scan_folder(source_folder, ignored_folders):
            try:
                category =  classifier(file_path ,config)
                new_path = file_mover(source_folder,file_path, category)

                logger.info(f"Moved {file_path.name} successfully New path: {new_path.parent}")
            except FileMoveError as e:
                logger.error(f"Failed to move {file_path.name}: {e}")
        logger.info("process ended")

    except Exception as unknown_error:
        logging.critical(f"Unknown error: {unknown_error}")

if __name__ == "__main__":
    main()





