from pathlib import Path


class FileHandler:

    def __init__(self, save_location: str):
        self.__save_location = save_location
        self.__init_dir()

    def __init_dir(self):
        Path(self.__save_location).mkdir(parents=True, exist_ok=True)

    def save(self, result: str, filename: str):
        if not result:
            return

        file = self.__save_location + filename
        with open(file, 'w+') as file:
            file.writelines(result)
