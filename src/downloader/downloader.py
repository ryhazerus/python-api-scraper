import requests
from requests import Response

from src.request_type_handlers.ResponseTypes import ResultType


class Scraper:
    """
    Scraper class is meant to take an url and result type (JSON or TEXT)
    as input and will retrieve the data at the given url endpoint. The
    Scraper has the option to either parse a json or text output at the
    url endpoint.
    """

    def __init__(self, url: str, response_type: ResultType = ResultType.JSON):
        self.__url: str = url
        self.__response_type = response_type
        self.__list_items: [str] = []

    def get_list(self):
        """
        Call a GET request on the given url.
        :return: the output of the endpoint if the status is 200/OK or None.
        """
        response = requests.get(self.__url)
        return self.__generic_response_handler(response)

    def get(self, url):
        """
        Single GET call with a generic formatter based
        on the response type provided in the class
        instantiation.
        :param url: the url to get the data from
        :return: the data based on the response type
        """
        response = requests.get(url)
        return self.__generic_response_handler(response)

    def __generic_response_handler(self, response):
        if response.status_code == 200:
            return self.__return_response(response)

        return None

    def __return_response(self, raw_response) -> Response:
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
                return NotImplemented

    @staticmethod
    def result_types():
        """
        Result request_type_handlers available for the GET request for parsing
        data at an endpoint.
        :return: list of available result request_type_handlers.
        """
        return [response for response in ResultType]
