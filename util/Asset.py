class Asset:
    def __init__(self, path: str):
        if not path.endswith("/"):
            path += "/"

        self.path = path
    
    def getByShortName(self, name: str) -> str:
        return self.path+name+"_image.png"
    
    def get(self, filename: str):
        with open(self.path + filename, "rb") as file:
            return file.read()