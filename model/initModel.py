#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
DBの初期化をします
"""

import Dao.pokemonListDao
import Dao.counterDao
import Dao.masterTimeDao

class InitModel:
    def init(self):
        """
        変数を取らず、Booleanを返します.
        """
        pokemonListFlag = Dao.pokemonListDao.init()
        CounterFlag = Dao.counterDao.init()
        if pokemonListFlag and CounterFlag:
            return True
        else:
            return False

    
    def initTime(self):
        """
        変数を取らず、Booleanを返します.
        """
        masterTimeFlag = Dao.masterTimeDao.init()
        return masterTimeFlag
