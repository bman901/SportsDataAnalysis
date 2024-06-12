"""File Manager class to create files and folders"""

import pathlib
import json
from Tools.Sports.sport_class import Sport as SportClass


class FileManager(SportClass):
    """File Manager class to create files and folders"""

    def create_folder(self, folder):
        """Creates a folder in which to store data"""
        path = pathlib.Path(folder)  # set folder filepath
        path.mkdir(parents=True, exist_ok=True)  # create folder
        return path

    def create_file(self, path, filename, result):
        """Creates a .json file with the data returned from an API request"""
        fn = filename + ".json"  # set up json file name
        filepath = path + "/" + fn  # set file filepath
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)  # create file
