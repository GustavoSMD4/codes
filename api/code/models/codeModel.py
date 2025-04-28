class Code:
    def __init__(self):
        self.__id: int = None
        self.__code: str = None
        self.__qtde: int = None
        
    @classmethod
    def newModel(cls, req: dict = None):
        if req is None:
            return cls()
        
        model = cls()
        model.__id = req.get("id")
        model.__code = req.get("code")
        model.__qtde = req.get("qtde")
        return model

    def getId(self):
        return self.__id

    def setId(self, id: int):
        self.__id = id

    def getCode(self):
        return self.__code

    def setCode(self, code: str):
        self.__code = code

    def getQtde(self):
        return self.__qtde

    def setQtde(self, qtde: int):
        self.__qtde = qtde

    def getDict(self):
        return {
            "id": self.__id,
            "code": self.__code,
            "qtde": self.__qtde
        }
