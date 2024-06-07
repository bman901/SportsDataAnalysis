import pathlib, json
from Tools.Sports.SportClass import Sport as SportClass

class FileManager(SportClass):
    def __init__(self, sport, version):
        super().__init__(sport, version)

    def create_folder(self, folder):
        path = pathlib.Path(folder) #set folder filepath
        path.mkdir(parents=True, exist_ok=True) #create folder
        return(path)

    def create_file(self, path, filename, result):
        fn = filename+".json" #set up json file name
        filepath = path+"/"+fn #set file filepath
        with open(filepath, "w", encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4) #create file