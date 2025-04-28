from flask import Flask, jsonify, request

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
        @self.app.route("/codes")
        def getCodes():
            try:
                if self.cache.getCodes() is not None:
                    return jsonify([code.getDict() for code in self.cache.getCodes()]), 200
                
                codes = self.__service.getCodes()
                return jsonify([code.getDict() for code in codes]), 200
                
            except Exception as e:
                return jsonify(str(e)), 400
            
        @self.app.route("/code/verify", methods=["POST"])
        def codeVerify():
            try:
                return jsonify(self.__service.verifyCodeSecurity(request.json)), 200
                
            except Exception as e:
                return jsonify(str(e)), 400

