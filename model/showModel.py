#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
メインページに表示する情報をDBから取ってくる機能を持ちます
"""

import Dao.counterDao
import Dao.pokemonListDao

class ShowModel:
    def __init__(self, mainViewInfo):
        self.mainViewInfo = mainViewInfo
        
    def show(self):
        """
        変数を取らず、mainViewInfoオブジェクトを返します
        """
        self.mainViewInfo = Dao.counterDao.getNumber(self.mainViewInfo)
        self.mainViewInfo.clefablePokemonList = Dao.pokemonListDao.getSortedByTime(5, u'ピクシーズ')
        self.mainViewInfo.gengarPokemonList = Dao.pokemonListDao.getSortedByTime(5, u'ゲンガーズ')
        return self.mainViewInfo