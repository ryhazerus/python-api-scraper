class FileHandler:

    def __init__(self, save_location: str):
        self.__save_location = save_location

    def save(self, text: str, filename: str):
        # Guard claus for handling empty texts
        if not text:
            return

        file = self.__save_location + filename
        with open(file, 'w+') as file:
            file.writelines(text)
