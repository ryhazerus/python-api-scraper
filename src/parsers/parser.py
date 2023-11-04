class Parser:

    def __init__(self, text: str, delimiter=","):
        self.__text = text
        self.__delimiter = delimiter

    @property
    def parsed_items(self):
        line_split = self.__text.split("\n")
        lines = ",".join(line_split)
        return lines.split(self.__delimiter)
