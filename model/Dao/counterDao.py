#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
（今のところ）
モデルはクラスを持たず、メソッドだけ入れておきます
DB1つに対して、1つのクラスといくつかのメソッドを持ちます
"""

from google.appengine.ext import ndb

class Counter(ndb.Model):
    team = ndb.StringProperty()
    number = ndb.IntegerProperty()
    time = ndb.DateTimeProperty(auto_now_add=True)
    
def increment(updateInfo):
    """
    変数にはupdateInfoオブジェクトをとる
    返却型は
    登録正常：True
    登録異常：False
    暫定的にはバリデーションかかっていないため、常にTrueを返す.
    """
    daoList = Counter.query(Counter.team == updateInfo.team).fetch(1)
    dao = daoList[0]
    dao.number = dao.number+1
    dao.put()
    return True

def getNumber(mainViewInfo):
    """
    変数にはmainViewInfoオブジェクトをとる
    返却型はmainViewInfo
    暫定的にはバリデーションかかっていないため、常にTrueを返す.
    """
    daoClefableList = Counter.query(Counter.team == u'ピクシーズ').fetch(1)
    mainViewInfo.clefableNumber = daoClefableList[0].number
    daoGengarList = Counter.query(Counter.team ==u'ゲンガーズ').fetch(1)
    mainViewInfo.gengarNumber = daoGengarList[0].number
    return mainViewInfo
    
    
    
    