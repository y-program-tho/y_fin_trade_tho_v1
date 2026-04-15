import logging

def setup_logging():

    logging.basicConfig(
        level=logging.info,
        format="%(asctime)s  %(levelname)s  %(name)s  %(message)s"
    )