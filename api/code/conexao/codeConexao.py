import os
import sqlite3

from api.code.models.codeModel import Code


class CodeConexao:
    def __init__(self):
        self.__conn = sqlite3.connect(os.path.join(os.getcwd(), "database", "database.db"), check_same_thread=False)
        self.__cursor = self.__conn.cursor()
        
    @classmethod
    def newConexao(cls):
        return cls()
    
    def getCodes(self):
        self.__cursor.execute("SELECT * FROM CODES;")
        return [Code.newModel(code) for code in self.__formatar()]
    
    def getCodeById(self, id):
        self.__cursor.execute("SELECT * FROM CODES WHERE ID = ?;", (id, ))
        codes = self.__formatar()
        return Code.newModel(codes[0])
    
    def getCodeByCode(self, code):
        self.__cursor.execute("SELECT * FROM CODES WHERE CODE = ?;", (code, ))
        codes = self.__formatar()
        return Code.newModel(codes[0])
        
    def __formatar(self):
        headers = [desc[0].lower() for desc in self.__cursor.description]
        dadosFormatados = [dict(zip(headers, data)) for data in self.__cursor.fetchall()]
        return dadosFormatados






