#!/usr/bin/env python
# coding:UTF-8
"""
ビューは必ず、メソッドの返却型を辞書型にする必要があります
"""

import common

class MainView():
    def __init__(self, mainViewInfo):
        self.clefableNumber = mainViewInfo.clefableNumber
        self.gengarNumber = mainViewInfo.gengarNumber
        self.pokemonList = mainViewInfo.pokemonList

    def getValues(self):
        """
        時間(秒)をHH:MMに変換して表示する
        """
        for datum in self.pokemonList:
            if datum.clefableFlag:
                datum.clefableStrTime = common.toHm(datum.clefableTime)
            if datum.gengarFlag:
                datum.gengarStrTime = common.toHm(datum.gengarTime)

        return {'clefableNumber':self.clefableNumber
               ,'gengarNumber':self.gengarNumber
               ,'pokemonList':self.pokemonList}