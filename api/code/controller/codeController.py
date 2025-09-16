import base64
from flask import Flask, jsonify, render_template, request

from api.code.service.codeService import CodeService
from cache.cache import Cache


class CodeController:
    def __init__(self, app, service, cache):
        self.__service: CodeService = service
        self.app: Flask = app
        self.cache: Cache = cache
    
    @classmethod
    def newController(cls, app, cache = None):
        return cls(app, CodeService.newService(cache), cache).routes()
    
    def routes(self):
        @self.app.route("/stats")
        def stats():
            try:
                return jsonify(self.__service.getStats()[0]), 200
                
            except Exception as e:
                return jsonify(str(e)), 400
        
        @self.app.route("/codes")
        def getCodes():
            try:
                if self.cache.getCodes() is not None:
                    return jsonify([code.getDict() for code in self.cache.getCodes()]), 200
                
                codes = self.__service.getCodes()
                return jsonify([code.getDict() for code in codes]), 200
                
            except Exception as e:
                return jsonify(str(e)), 400
            
        @self.app.route("/code/verify/<code>")
        def codeVerify(code):
            try:
                return jsonify(self.__service.verifyCodeSecurity({"code": code})), 200
                
            except Exception as e:
                return jsonify(str(e)), 400
            
        @self.app.route("/codes/first/<int:limit>")
        def getCodesLimitFirst(limit):
            try:
                return jsonify([code.getDict() for code in self.__service.getCodesLimitFirst({"limit": limit})]), 200
                
            except Exception as e:
                return jsonify(str(e)), 400
            
        @self.app.route("/codes/last/<int:limit>")
        def getCodesLimitLast(limit):
            try:
                return jsonify([code.getDict() for code in self.__service.getCodesLimitLast({"limit": limit})]), 200
                
            except Exception as e:
                return jsonify(str(e)), 400

        @self.app.route("/code/suggest")
        def suggestCode():
            try:
                code = self.__service.suggestCode({"safe": request.args.get("safe")})
                return jsonify(code.getCode()), 200
                
            except Exception as e:
                return jsonify(str(e)), 400

        @self.app.route("/codes/planilha/<digits>")
        def gerarPlanilha(digits):
            try:
                arquivo = self.__service.gerarPlanilha(digits)
                base64Excel = base64.b64encode(arquivo.read()).decode("utf-8")
                return render_template("download.html", base64Excel=base64Excel)
                
            except Exception as e:
                return jsonify(str(e)), 400
            
        @self.app.route("/codes/csv")
        def gerarCSV():
            try:
                arquivo = self.__service.gerarCSVCompleto()
                base64CSV = base64.b64encode(arquivo.read()).decode("utf-8")
                return render_template("download_csv.html", base64CSV=base64CSV)

            except Exception as e:
                return jsonify(str(e)), 400

