class Parser:

    def __init__(self, text: str, delimiter: str = ","):
        self.__text = text
        self.__delimiter = delimiter

    def parsed_items(self):
        line_split = self.__text.split("\n")
        lines = self.__delimiter.join(line_split)
        item_per_line = lines.split(self.__delimiter)

        return [item.strip() for item in item_per_line if len(item)]
