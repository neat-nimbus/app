#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
DBに捕まえたポケモンの情報を登録する機能を持ちます
"""

import Dao.pokemonListDao
import Dao.counterDao
import logging

class RegisterModel():
    def __init__(self, updateInfo):
        self.updateInfo = updateInfo

    def register(self):
        """
        変数を取らず、登録正常かどうかのフラグを返します.
        登録正常：True
        登録異常：False
        """
        if (self.updateInfo.team == u'ピクシーズ' or self.updateInfo.team == u'ゲンガーズ'):
            flag = Dao.pokemonListDao.register(self.updateInfo)
            if flag:
                Dao.counterDao.increment(self.updateInfo)
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
    
        