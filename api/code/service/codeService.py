
from api.code.conexao.codeConexao import CodeConexao
from cache.cache import Cache


class CodeService:
    def __init__(self, conexao, cache):
        self.__conexao: CodeConexao = conexao
        self.cache: Cache = cache
        
    @classmethod
    def newService(cls, cache = None):
        return cls(CodeConexao.newConexao(), cache)
    
    def getCodes(self):
        codes = self.__conexao.getCodes()
        self.cache.setCodes(codes)
        return codes
        

