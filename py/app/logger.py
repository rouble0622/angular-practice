import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(app):
    log_folder = "logs"
    os.makedirs(log_folder, exist_ok=True)

    log_file = os.path.join(log_folder, "app.log")

    handler = RotatingFileHandler(log_file, maxBytes=1000000, backupCount=3)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
