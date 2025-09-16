from io import BytesIO
import random

from openpyxl import Workbook
from openpyxl.worksheet.datavalidation import DataValidation
from api.code.conexao.codeConexao import CodeConexao
from api.code.models.codeModel import Code
from cache.cache import Cache


class CodeService:
    def __init__(self, conexao, cache):
        self.__conexao: CodeConexao = conexao
        self.cache: Cache = cache
        
    @classmethod
    def newService(cls, cache = None):
        return cls(CodeConexao.newConexao(), cache)
    
    def getStats(self):
        return self.__conexao.stats()
    
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
    
    def suggestCode(self, req: dict):
        safe = req.get("safe")
        
        if safe == "True":
            safe = True
        elif safe == "False":
            safe = False
        else:
            raise Exception("param safe needs to be True or False.")
        
        codes = self.__conexao.suggestCode(safe)
        return Code.newModel(random.choice(codes))
    
    def gerarPlanilha(self, digits = None):
        if digits is None:
            digits = 3
            
        codes = self.__conexao.getCodes()
        vistos = set()
        resultado = []

        for code in codes:
            prefixo = code.getCode()[:digits]
            if prefixo not in vistos:
                vistos.add(prefixo)
                resultado.append(prefixo)
                
        wb = Workbook()
        ws = wb.active
        ws.title = "codigos"

        # Cabeçalhos
        ws.append(["codigo", "feito"])

        checkValidation = DataValidation(type="list", formula1='"TRUE,FALSE"', allow_blank=True)
        ws.add_data_validation(checkValidation)

        for index, codigo in enumerate(resultado, start=2):
            ws[f"A{index}"] = codigo
            cellCheck = f"B{index}"
            checkValidation.add(ws[cellCheck])
            ws[cellCheck] = "FALSE"
        
        output = BytesIO()
        wb.save(output)
        output.seek(0)
        return output
    
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
    
        
        
        

