import os
import time
import logging
import schedule
from typing import List
from utils.plugins import search_for_plugins
from utils.adapters import DataAdapter

from src.utils.adapter_abstract import AbstractAdapter

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.DEBUG)


def run_plugins_job(db: AbstractAdapter, available_plugins: List):
    for plugin in available_plugins:
        try:
            logger.info(f'Running plugin {plugin.__name__} ')
            instance = plugin(db=db)
            instance.run()
            logger.info(f"Plugin {plugin.__name__} finished successfully")
        except Exception as ex:
            logger.error(f'Error running plugin {plugin.__name__}, exception: {ex}')


def main():
    db = DataAdapter.get_adapter()
    available_plugins = search_for_plugins()

    # run once
    run_plugins_job(db=db, available_plugins=available_plugins)
    # run every day at 2am
    schedule.every().day.at("02:00").do(run_plugins_job, db=db, available_plugins=available_plugins)

    logging.debug('Run schedule job every day at 02:00')
    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__ == "__main__":
    main()
