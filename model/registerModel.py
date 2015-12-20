#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
DBに捕まえたポケモンの情報を登録する機能を持ちます
"""

import Dao.pokemonListDao
import Dao.counterDao
import Dao.masterTimeDao
import logging
from datetime import datetime, timedelta


def get_time():
    """
    捕獲までの時間を返す関数.単位は秒(int)
    """
    nowDateTime = datetime.now() + timedelta(hours=9)
    startDateTime = Dao.masterTimeDao.getTime()
    deltaDateTime = nowDateTime - startDateTime
    seconds = int(deltaDateTime.total_seconds())
    
    START = [0, 7200, 16200, 23100, 30000, 36900, 45900, 52800]
    END = [6300, 13500, 22500, 29400, 36300, 43200, 52200, 59100]
    DELTA = [0, 900, 3600, 4200, 4800, 5400, 8100, 8700, 9300, 9900]
    
    START.append(seconds)
    START.sort()
    i = START.index(seconds)-1
    seconds = seconds - DELTA[i]
    
    return seconds


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
            self.updateInfo.time = get_time()
            logging.info(self.updateInfo.time)
            
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
    
        