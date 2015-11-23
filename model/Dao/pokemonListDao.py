#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
（今のところ）
モデルはクラスを持たず、メソッドだけ入れておきます
DB1つに対して、1つのクラスといくつかのメソッドを持ちます
"""

from google.appengine.ext import ndb

class PokemonList(ndb.Model):
    team = ndb.StringProperty()
    pokemon = ndb.StringProperty()
    time = ndb.DateTimeProperty(auto_now_add=True)
    
def register(updateInfo):
    """
    変数にはupdateInfoオブジェクトをとる
    返却型は
    登録正常：True
    登録異常：False
    暫定的にはバリデーションかかっていないため、常にTrueを返す.
    """
    dao = PokemonList()
    dao.team = updateInfo.team
    dao.pokemon = updateInfo.pokemon
    dao.put()
    return True