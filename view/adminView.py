#!/usr/bin/env python
# coding:UTF-8
"""
ビューは必ず、メソッドの返却型を辞書型にする必要があります
"""

class AdminView():
    def __init__(self, initFlag):
        self.initFlag = initFlag
        
    def getValues(self):
        if self.initFlag:
            return {'message':u'DBの初期化に成功しました'}
        else:
            return {'message':u'DBの初期化に失敗しました.ログを参照してください'}

class ErrorView():
    def getValues(self):
        return {'message':u'パスワードが違います'}