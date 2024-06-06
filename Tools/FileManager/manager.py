import pathlib, json

from Tools.APICaller import caller

class FileManager(object):
    def __init__(self, sport, version):
        self.sport = sport
        self.version = version

    def create_folder(self, folder):
        path = pathlib.Path(folder) #set folder filepath
        path.mkdir(parents=True, exist_ok=True) #create folder
        return(path)
        
    def create_file(self, path, filename, result):
        fn = filename+".json" #set up json file name
        filepath = path+"/"+fn #set file filepath
        with open(filepath, "w", encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4) #create file

    def download_data(self, folder, call, qualifiers=""):
        response = caller.APICall.API_request(call, qualifiers)
        if "/" in call:
            self.create_file(folder, str(call).capitalize().rsplit("/", 1)[1], response) #Set the filename to anything beyond the '/' in the call, then create data file
        else:
            self.create_file(folder, str(call).capitalize(), response) #Create data file within folder