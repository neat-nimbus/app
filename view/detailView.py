#!/usr/bin/env python
# coding:UTF-8
"""
ビューは必ず、メソッドの返却型を辞書型にする必要があります
"""

class DetailView():
    def __init__(self, detailViewInfo):
        self.detailViewInfo = detailViewInfo

    def getValues(self):
        return {'detailViewInfo' : self.detailViewInfo}