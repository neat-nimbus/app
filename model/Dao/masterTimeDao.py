#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
（今のところ）
モデルはクラスを持たず、メソッドだけ入れておきます
DB1つに対して、1つのクラスといくつかのメソッドを持ちます
"""

from google.appengine.ext import ndb
import logging
from datetime import datetime, timedelta

class MasterTime(ndb.Model):
    time = ndb.DateTimeProperty()

def init():
    """
    dbの初期状態を作成する.すでに初期化されている場合は異常を返す
    変数は取らない
    返却型はBooleanで初期化成功はTrue、失敗はFalse
    """
    key = ndb.Key('MasterTime', 'masterTime')
    dao = key.get()
    if dao == None:
        dao1 = MasterTime(id='masterTime')
        dao1.time = datetime.now() + timedelta(hours=9)
        dao1.put()
        logging.info(u"masterTimeの初期化に成功しました")
        return True
    else:
        logging.warning(u"すでにmasterTimeは初期化されています")
        return False
        
def getTime():
    """
    スタート時刻を呼び出す
    """
    return MasterTime.query().fetch()[0].time
