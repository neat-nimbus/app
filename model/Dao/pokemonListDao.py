#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
（今のところ）
モデルはクラスを持たず、メソッドだけ入れておきます
DB1つに対して、1つのクラスといくつかのメソッドを持ちます
"""

from google.appengine.ext import ndb
import logging

class PokemonList(ndb.Model):
    pokemon = ndb.StringProperty()
    normalOrder = ndb.IntegerProperty()
    clefableFlag = ndb.BooleanProperty()
    clefableTime = ndb.TimeProperty()
    gengarFlag = ndb.BooleanProperty()
    gengarTime = ndb.TimeProperty()

    
def init():
    """
    dbの初期状態を作成する.すでに初期化されている場合は異常を返す
    変数は取らない
    返却型はBooleanで初期化成功はTrue、失敗はFalse
    """
    key = ndb.Key('PokemonList', u'フシギダネ')
    dao = key.get()
    if dao == None:
        daoList = []
        for normalOrder, pokemon in enumerate(POKEMON_LIST):
            dao = PokemonList(id=pokemon)
            dao.normalOrder = normalOrder
            dao.pokemon = pokemon
            dao.clefableFlag = False
            dao.gengarFlag = False
            daoList.append(dao)
        ndb.put_multi(daoList)
        logging.info("PokemonListの初期化に成功しました")
        return True
    else:
        logging.warning("すでにPokemonListは初期化されています")
        return False


def register(updateInfo):
    """
    変数にはupdateInfoオブジェクトをとる
    返却型はBooleanで登録成功はTrue、失敗はFalse
    登録時刻部分はまだ実装していない
    """
    key = ndb.Key('PokemonList', updateInfo.pokemon)
    dao = key.get()
    if dao != None:
        if updateInfo.team == u'ピクシーズ':
            if dao.clefableFlag == False:
                dao.clefableFlag = True
                #dao.clefableTime = updateInfo.time
                dao.put()
                return True
            else:
                logging.error("ピクシーズのそのポケモンはすでに捕獲されています")
                return False
        elif updateInfo.team == u'ゲンガーズ':
            if dao.gengarFlag == False:
                dao.gengarFlag = True
                #dao.gengarTime = updateInfo.time
                dao.put()
                return True
            else:
                logging.error("ゲンガーズのそのポケモンはすでに捕獲されています")
                return False
    else:
        logging.error("ポケモン名が不正で、DBから正しく取得できません")
        return False


def getAllSortedByNormalOrder():
    """
    変数はとらない
    返却型はPokemonListのリスト型
    """
    return PokemonList.query().order(PokemonList.normalOrder).fetch()


POKEMON_LIST = (u'フシギダネ',
u'フシギソウ',
u'フシギバナ',
u'ヒトカゲ',
u'リザード',
u'リザードン',
u'ゼニガメ',
u'カメール',
u'カメックス',
u'キャタピー',
u'トランセル',
u'バタフリー',
u'ビードル',
u'コクーン',
u'スピアー',
u'ポッポ',
u'ピジョン',
u'ピジョット',
u'コラッタ',
u'ラッタ',
u'オニスズメ',
u'オニドリル',
u'アーボ',
u'アーボック',
u'ピカチュウ',
u'ライチュウ',
u'サンド',
u'サンドパン',
u'ニドラン♀',
u'ニドリーナ',
u'ニドクイン',
u'ニドラン♂',
u'ニドリーノ',
u'ニドキング',
u'ピッピ',
u'ピクシー',
u'ロコン',
u'キュウコン',
u'プリン',
u'プクリン',
u'ズバット',
u'ゴルバット',
u'ナゾノクサ',
u'クサイハナ',
u'ラフレシア',
u'パラス',
u'パラセクト',
u'コンパン',
u'モルフォン',
u'ディグダ',
u'ダグトリオ',
u'ニャース',
u'ペルシアン',
u'コダック',
u'ゴルダック',
u'マンキー',
u'オコリザル',
u'ガーディ',
u'ウインディ',
u'ニョロモ',
u'ニョロゾ',
u'ニョロボン',
u'ケーシィ',
u'ユンゲラー',
u'フーディン',
u'ワンリキー',
u'ゴーリキー',
u'カイリキー',
u'マダツボミ',
u'ウツドン',
u'ウツボット',
u'メノクラゲ',
u'ドククラゲ',
u'イシツブテ',
u'ゴローン',
u'ゴローニャ',
u'ポニータ',
u'ギャロップ',
u'ヤドン',
u'ヤドラン',
u'コイル',
u'レアコイル',
u'カモネギ',
u'ドードー',
u'ドードリオ',
u'パウワウ',
u'ジュゴン',
u'ベトベター',
u'ベトベトン',
u'シェルダー',
u'パルシェン',
u'ゴース',
u'ゴースト',
u'ゲンガー',
u'イワーク',
u'スリープ',
u'スリーパー',
u'クラブ',
u'キングラー',
u'ビリリダマ',
u'マルマイン',
u'タマタマ',
u'ナッシー',
u'カラカラ',
u'ガラガラ',
u'サワムラー',
u'エビワラー',
u'ベロリンガ',
u'ドガース',
u'マタドガス',
u'サイホーン',
u'サイドン',
u'ラッキー',
u'モンジャラ',
u'ガルーラ',
u'タッツー',
u'シードラ',
u'トサキント',
u'アズマオウ',
u'ヒトデマン',
u'スターミー',
u'バリヤード',
u'ストライク',
u'ルージュラ',
u'エレブー',
u'ブーバー',
u'カイロス',
u'ケンタロス',
u'コイキング',
u'ギャラドス',
u'ラプラス',
u'メタモン',
u'イーブイ',
u'シャワーズ',
u'サンダース',
u'ブースター',
u'ポリゴン',
u'オムナイト',
u'オムスター',
u'カブト',
u'カブトプス',
u'プテラ',
u'カビゴン',
u'フリーザー',
u'サンダー',
u'ファイヤー',
u'ミニリュウ',
u'ハクリュー',
u'カイリュー',
u'ミュウツー')