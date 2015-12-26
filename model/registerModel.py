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
    
    START = [0, 6900, 16200, 23100, 30000, 36900, 46200, 53100]
    END = [6300, 13200, 22500, 29400, 36300, 43200, 52500, 59400]
    DELTA = [0, 600, 3600, 4200, 4800, 5400, 8400, 9000, 9600, 10200]
    
    START.append(seconds)
    END.append(seconds)
    START.sort()
    END.sort()
    i = START.index(seconds)-1
    j = END.index(seconds)
    if i == j:
        seconds = seconds - DELTA[i]
    else:
        seconds = END[i] - DELTA[i]    
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
    
        