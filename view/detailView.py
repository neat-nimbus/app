#!/usr/bin/env python
# coding:UTF-8
"""
ビューは必ず、メソッドの返却型を辞書型にする必要があります
"""

import logging
import common

class DetailView():
    def __init__(self, detailViewInfo):
        self.detailViewInfo = detailViewInfo

    def getValues(self):
        """
        時間(秒)をHH:MM:SSに変換して表示する
        """
        for datum in self.detailViewInfo:
            if datum.clefableFlag:
                datum.clefableStrTime = common.toHm(datum.clefableTime)
            if datum.gengarFlag:
                datum.gengarStrTime = common.toHm(datum.gengarTime)
            datum.nicoStrTime = common.toHm(datum.nicoTime)
        return {'detailViewInfo' : self.detailViewInfo}