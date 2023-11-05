import concurrent
import time

import requests

from src.handler.handler import FileHandler
from src.response_type_handlers.ResponseTypes import ResultType
from src.utils import pretty_log


class Scraper:
    """
    Scraper class is meant to take an url and result type (JSON or TEXT)
    as input and will retrieve the data at the given url endpoint. The
    Scraper has the option to either parse a json or text output at the
    url endpoint.
    """

    def __init__(self, url: str, save_location: str, result_type: ResultType = ResultType.JSON):
        self.__url: str = url
        self.__delay = 1
        self.__response_type = result_type
        self.__save_location = save_location

        self.__file_handler = FileHandler(self.__save_location)

    def start(self, uris: [str], save_to_file=False):
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            processes = []
            pretty_log("Starting download...")
            for uri in uris:
                endpoint = f"{self.__url}{uri}"
                pretty_log(f"Spawning process for {endpoint}")
                processes.append(executor.submit(self.__get, endpoint, save_to_file, uri, ))

            results = concurrent.futures.as_completed(processes)

            finished_results = [process.result() for process in results]
            pretty_log("All downloads completed")
            
            return finished_results

    def __get(self, *args):
        """
        Single GET call with a generic formatter based
        on the response type provided in the class
        instantiation.
        :param url: the url to get the data from
        :return: the data based on the response type
        """
        if len(args) < 3:
            pretty_log("Arguments for start do not match")
            return

        url, save_to_file, uri = args

        time.sleep(self.__delay)

        response = requests.get(url)
        parsed_response = self.__generic_response_handler(response)

        if save_to_file and parsed_response is not None:
            self.__file_handler.save(parsed_response, uri)

        return parsed_response

    def __generic_response_handler(self, response):
        """
         Response handler for successful calls.
        :param response: the raw response.
        :return: None if request is not successful
        the given request return type.
        """
        if response.status_code == 200:
            return self.__return_response(response)

        return None

    def __return_response(self, raw_response):
        """
        Match the type of return value to the data expected to be
        at the end of the endpoint.
        :param raw_response: the raw response from the get request
        :return: the response converted in the type expected.
        """
        match self.__response_type:
            case ResultType.JSON:
                return raw_response.json()
            case ResultType.TEXT:
                return raw_response.text
            case _:
                return None

    @staticmethod
    def result_types():
        """
        Result response_type_handlers available for the GET request for parsing
        data at an endpoint.
        :return: list of available result response_type_handlers.
        """
        return [response for response in ResultType]
