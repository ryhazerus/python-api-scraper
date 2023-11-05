from src.scraper.scraper import Scraper
from src.parsers.parser import Parser
from src.response_type_handlers.ResponseTypes import ResultType

BASE_URL = "https://www.toptal.com/developers/gitignore/api/"
SAVE_LOCATION = "./output/"

if __name__ == '__main__':
    scraper = Scraper(BASE_URL, SAVE_LOCATION, result_type=ResultType.TEXT)
    parsed_items = Parser(scraper.start(['list'], True)[0]).parsed_items()

    scraper.start(parsed_items, save_to_file=True)
