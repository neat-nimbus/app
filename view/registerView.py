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

    def getValues(self, mode):
        self.pokemon.encode('utf_8')
        self.team.encode('utf_8')
        if mode == "register":
            message = self.team + u'が' + self.pokemon + u'を捕まえました。'
        elif mode == "delete":
            message = self.team + u'が' + self.pokemon + u'を削除しました。'
        
        return {'message':message }


class ErrorView():
    """
    本来は、errorによってメッセージを出し分けるべき.
    """
    def getValues(self, mode):
        if mode == "register":
            return {'message':u'不正な登録です。ポケモン名が違うか、そのポケモンはすでに登録されています。'}
        elif mode == "delete":
            return {'message':u'不正な削除です。ポケモン名が違うか、そのポケモンはまだ登録されていません。'}