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
        self.clefablePokemonList = mainViewInfo.clefablePokemonList
        self.gengarPokemonList = mainViewInfo.gengarPokemonList

    def getValues(self):
        """
        時間(秒)をHH:MMに変換して表示する
        """
        for c, g in zip(self.clefablePokemonList, self.gengarPokemonList):
            if c.clefableFlag:
                c.clefableStrTime = common.toHm(c.clefableTime)
            if g.gengarFlag:
                g.gengarStrTime = common.toHm(g.gengarTime)

        return {'clefableNumber':self.clefableNumber
               ,'gengarNumber':self.gengarNumber
               ,'clefablePokemonList':self.clefablePokemonList
               ,'gengarPokemonList':self.gengarPokemonList}