
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
    
    def verifyCodeSecurity(self, req: dict):
        code: str = req.get("code")
        
        if not isinstance(code, str):
            code = str(code)
        
        if code is None:
            raise Exception("code empty")
        
        if len(code) != 4 or not code.isdigit():
            raise Exception("code needs to have 4 digits")
        
        codeDb = self.__conexao.getCodeByCode(code)
        
        return f"Your code is the number {codeDb.getId()} most used out of 10000."
        
        
        
        

