#!/usr/bin/env python
# coding:UTF-8
"""
ビューは必ず、メソッドの返却型を辞書型にする必要があります
"""

class MainView():
    def __init__(self, mainViewInfo):
        self.clefableNumber = mainViewInfo.clefableNumber
        self.gengarNumber = mainViewInfo.gengarNumber
        #self.pokemonList = mainView.pokemonList

    def getValues(self):
        #for pokemon in self.pokemonList:
            #pokemon.encode('utf_8')
        #return {'clefableNumber':self.clefableNumber,'gengarNumber':self.gengarNumber,'pokemonList':self.pokemonList}
        return {'clefableNumber':self.clefableNumber
               ,'gengarNumber':self.gengarNumber}