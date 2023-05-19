import logging
from datetime import datetime

import pytz

from vectordb import get_collection
from extractor import extract_data
from loader import load_data
from settings import settings
from state import State, JsonFileStorage
from transformer import transform_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
)


def init():
    """
    Initialize DB: Extract, Transform and Load data
    """

    collection = get_collection(settings.INDEX_NAME)

    filename = "etl/documentation.json"
    logging.info("Extracting data")
    raw_data = extract_data(filename)
    logging.info("Transforming data")
    transformed_data = transform_data(raw_data)
    logging.info("Loading data")
    load_data(collection, transformed_data)


def main():
    storage = JsonFileStorage()
    state = State(storage=storage)

    is_init = state.get_state("init")

    if not is_init:
        logging.info("Starting initialization of the ETL")
        init()
        state.set_state("init", True)
        utc_now = datetime.now(pytz.utc)
        utc_now_iso = datetime.isoformat(utc_now)
        state.set_state("last_modified", utc_now_iso)
        storage.save_state(state.local_state)
        logging.info("Finished initialization of the ETL")


if __name__ == "__main__":
    main()
