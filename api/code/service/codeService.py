
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
    
    def getCodesLimitFirst(self, req: dict):
        limit = req.get("limit")
        
        if not isinstance(limit, int):
            limit = int(limit)
            
        if limit > 10000 or limit <= 0:
            raise Exception("limit needs to be between 1 and 10000")
        
        return self.__conexao.getCodesLimit(limit)
    
    def getCodesLimitLast(self, req: dict):
        limit = req.get("limit")
        
        if not isinstance(limit, int):
            limit = int(limit)
            
        if limit > 10000 or limit <= 0:
            raise Exception("limit needs to be between 1 and 10000")
        
        return self.__conexao.getCodesLimit(limit, False)
        
    
    def verifyCodeSecurity(self, req: dict):        
        code: str = self.__validateCode(req.get("code"))
        
        codeDb = self.__conexao.getCodeByCode(code)
        
        return f"Your code is the number {codeDb.getId()} most used out of 10000."
    
    def simulateBruteForce(self, req: dict):
        code: str = self.__validateCode(req.get("code"))
    
    @staticmethod
    def __validateCode(code):
        if not isinstance(code, str):
            code = str(code)
        
        if code is None:
            raise Exception("code empty")
        
        if len(code) != 4 or not code.isdigit():
            raise Exception("code needs to have 4 digits")
        
        return code
    
        
        
        

