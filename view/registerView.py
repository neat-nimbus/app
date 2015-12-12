#!/usr/bin/env python
# coding:UTF-8
"""
ビューは必ず、メソッドの返却型を辞書型にする必要があります
"""

class RegisterView():
    def __init__(self, registerViewInfo):
        self.registerViewInfo = registerViewInfo

    def getValues(self):
        return {'registerViewInfo' : self.registerViewInfo}