from unittest import TestCase

from src.parsers.parser import Parser


class TestParser(TestCase):

    def setUp(self):
        self.text = ("pokemon,beer, humans,dog+breeds,cocktails\n"
                     "car+brands,names,uniforms,sector")

    def test_parsed_items(self):
        parser = Parser(self.text)

        expected_result = ["pokemon", "beer", "humans", "dog+breeds",
                           "cocktails", "car+brands", "names", "uniforms", "sector"]

        actual_result = parser.parsed_items()

        self.assertEquals(expected_result, actual_result)
