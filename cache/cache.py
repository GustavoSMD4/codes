from api.code.models.codeModel import Code


class Cache:
    def __init__(self):
        self.__codes: list[Code] = None
        
    def getCodes(self):
        return self.__codes
    
    def setCodes(self, codes: list[Code]):
        self.__codes = codes
    
    
    