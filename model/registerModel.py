#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
DBに捕まえたポケモンの情報を登録する機能を持ちます
"""

import Dao.pokemonListDao
import Dao.counterDao

class RegisterModel:
    def __init__(self, updateInfo):
        self.updateInfo = updateInfo

    def register(self):
        """
        変数を取らず、updateInfoオブジェクトを返します
        """
        if (self.updateInfo.team == u'ピクシーズ' or self.updateInfo.team == u'ゲンガーズ'):
            Dao.counterDao.increment(self.updateInfo)
            Dao.pokemonListDao.register(self.updateInfo)
            return self.updateInfo
        else:
            """
            異常時ハンドリングはまだ
            """
            pass