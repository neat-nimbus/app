#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
（今のところ）
モデルはクラスを持たず、メソッドだけ入れておきます
DB1つに対して、1つのクラスといくつかのメソッドを持ちます
"""

from google.appengine.ext import ndb
import logging

class Counter(ndb.Model):
    number = ndb.IntegerProperty()
    time = ndb.DateTimeProperty(auto_now_add=True)
    
def init():
    """
    dbの初期状態を作成する.すでに初期化されている場合は異常を返す
    変数は取らない
    返却型はBooleanで初期化成功はTrue、失敗はFalse
    """
    key = ndb.Key('Counter', u'ピクシーズ')
    dao = key.get()    
    if dao == None:
        dao1 = Counter(id=u'ピクシーズ')
        dao1.number = 0
        dao2 = Counter(id=u'ゲンガーズ')
        dao2.number = 0
        daoList = [dao1, dao2]
        ndb.put_multi(daoList)
        logging.info("Counterの初期化に成功しました")
        return True
    else:
        logging.warning("すでにCounterは初期化されています")
        return False        

    
def increment(updateInfo):
    """
    変数にはupdateInfoオブジェクトをとる
    返却型はBooleanで成功はTrue、失敗はFalse
    """
    key = ndb.Key('Counter', updateInfo.team)
    dao = key.get()
    if dao != None:
        dao.number = dao.number+1
        dao.put()
        return True
    else:
        logging.error("チーム名が不正で、DBから正しく取得できません")
        return False
        

def getNumber(mainViewInfo):
    """
    変数にはmainViewInfoオブジェクトをとる
    返却型はmainViewInfo
    暫定的にはバリデーションかかっていないため、常にTrueを返す.
    """
    keys = [ndb.Key('Counter', u'ピクシーズ'), ndb.Key('Counter', u'ゲンガーズ')]
    daos = ndb.get_multi(keys)
    
    mainViewInfo.clefableNumber = daos[0].number
    mainViewInfo.gengarNumber = daos[1].number
    return mainViewInfo