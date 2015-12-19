#!/usr/bin/env python
# coding:UTF-8
"""
ビューは必ず、メソッドの返却型を辞書型にする必要があります
"""

class InitView():
    def __init__(self, registerViewInfo):
        self.registerViewInfo = registerViewInfo

    def getValues(self):
        return {'registerViewInfo' : self.registerViewInfo}


class RegisterView():
    def __init__(self, updateInfo):
        self.pokemon = updateInfo.pokemon
        self.team = updateInfo.team

    def getValues(self):
	self.pokemon.encode('utf_8')
	self.team.encode('utf_8')
        return {'getPokemon':self.pokemon, 'getTeam':self.team}

class ErrorView():
    """
    本来は、errorによってメッセージを出し分けるべき.
    """
    def getValues(self):
        return {'message':u'不正な登録です。ポケモン名が違うか、そのポケモンはすでに登録されています。'}