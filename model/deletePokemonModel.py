#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
DBに捕まえたポケモンの情報を登録する機能を持ちます
"""

import Dao.pokemonListDao
import Dao.counterDao
import Dao.masterTimeDao
import logging


class DeletePokemonModel():
    def __init__(self, updateInfo):
        self.updateInfo = updateInfo        


    def delete(self):
        """
        変数を取らず、削除正常かどうかのフラグを返します.
        削除正常：True
        削除異常：False
        """
        if (self.updateInfo.team == u'ピクシーズ' or self.updateInfo.team == u'ゲンガーズ'):

            flag = Dao.pokemonListDao.delete(self.updateInfo)
            if flag:
                Dao.counterDao.decrement(self.updateInfo)
                return True
            else:
                """
                異常時ハンドリングはまだ
                """
                return False
        else:
            """
            異常時ハンドリングはまだ
            """
            return False
    
        