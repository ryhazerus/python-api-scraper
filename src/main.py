import time
from pathlib import Path

from src.downloader.downloader import Scraper
from src.handler.handler import FileHandler
from src.parsers.parser import Parser
from src.response_type_handlers.ResponseTypes import ResultType

TIME_DELAY = 1
LIST_URL = "https://www.toptal.com/developers/gitignore/api/list"
BASE_URL = "https://www.toptal.com/developers/gitignore/api"
SAVE_LOCATION = "./output/"


def pretty_log(msg: str):
    print(f"[INFO]:\t{msg}")


if __name__ == '__main__':
    # Create output DIR
    Path(SAVE_LOCATION).mkdir(parents=True, exist_ok=True)

    # Provide download link
    downloader = Scraper(LIST_URL, response_type=ResultType.TEXT)

    # Get the text from the provided list
    list_response = downloader.get_list()

    # Parse the provided raw text (list of comma separated items)
    parser = Parser(list_response)

    pretty_log(f"There are {len(parser.parsed_items)} to be downloaded")

    # For each item in the list get the data from the endpoint
    pretty_log("Starting download now...")

    file_handler = FileHandler(SAVE_LOCATION)
    for uri in parser.parsed_items:
        pretty_log(f"Downloading {uri}")

        formatted_url = f"{BASE_URL}/{uri}"
        result = downloader.get(formatted_url)

        file_handler.save(result, uri)
        time.sleep(TIME_DELAY)
