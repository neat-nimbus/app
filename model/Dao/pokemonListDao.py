#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
（今のところ）
モデルはクラスを持たず、メソッドだけ入れておきます
DB1つに対して、1つのクラスといくつかのメソッドを持ちます
"""

from google.appengine.ext import ndb
import logging
import copy

class PokemonList(ndb.Model):
    pokemon = ndb.StringProperty()
    normalOrder = ndb.IntegerProperty()
    gengarOrder = ndb.IntegerProperty()
    clefableFlag = ndb.BooleanProperty()
    clefableTime = ndb.IntegerProperty()
    gengarFlag = ndb.BooleanProperty()
    gengarTime = ndb.IntegerProperty()
    nicoFlag = ndb.BooleanProperty()
    nicoTime = ndb.IntegerProperty()
    
    
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
        for normalOrder, (pokemon, gengarOrder, nicoTime) in enumerate(zip(POKEMON_LIST, GENGARS_ORDER, NICO_TIMES)):
            dao = PokemonList(id=pokemon)
            dao.normalOrder = normalOrder
            dao.gengarOrder = gengarOrder
            dao.pokemon = pokemon
            dao.clefableFlag = False
            dao.gengarFlag = False
            dao.nicoFlag = True
            dao.nicoTime = nicoTime
            daoList.append(dao)
        ndb.put_multi(daoList)
        logging.info(u"PokemonListの初期化に成功しました")
        return True
    else:
        logging.warning(u"すでにPokemonListは初期化されています")
        return False


def register(updateInfo):
    """
    変数にはupdateInfoオブジェクトをとる
    返却型はBooleanで登録成功はTrue、失敗はFalse
    登録時刻部分はまだ実装していない
    """
    if updateInfo.pokemon != '':
        key = ndb.Key('PokemonList', updateInfo.pokemon)
        dao = key.get()
        if dao != None:
            if updateInfo.team == u'ピクシーズ':
                if dao.clefableFlag == False:
                    dao.clefableFlag = True
                    dao.clefableTime = updateInfo.time
                    dao.put()
                    return True
                else:
                    logging.error(u"ピクシーズのそのポケモンはすでに捕獲されています")
                    return False
            elif updateInfo.team == u'ゲンガーズ':
                if dao.gengarFlag == False:
                    dao.gengarFlag = True
                    dao.gengarTime = updateInfo.time
                    dao.put()
                    return True
                else:
                    logging.error(u"ゲンガーズのそのポケモンはすでに捕獲されています")
                    return False
        else:
            logging.error(u"ポケモン名が不正で、DBから正しく取得できません")
            return False
    else:
        logging.error(u"ポケモン名がブランクです")


def delete(updateInfo):
    """
    変数にはupdateInfoオブジェクトをとる
    返却型はBooleanで登録成功はTrue、失敗はFalse
    登録時刻部分はまだ実装していない
    """
    if updateInfo.pokemon != '':
        key = ndb.Key('PokemonList', updateInfo.pokemon)
        dao = key.get()
        if dao != None:
            if updateInfo.team == u'ピクシーズ':
                if dao.clefableFlag == True:
                    dao.clefableFlag = False
                    dao.clefableTime = None
                    dao.put()
                    return True
                else:
                    logging.error(u"ピクシーズのそのポケモンはまだ捕獲されていません")
                    return False
            elif updateInfo.team == u'ゲンガーズ':
                if dao.gengarFlag == True:
                    dao.gengarFlag = False
                    dao.gengarTime = None
                    dao.put()
                    return True
                else:
                    logging.error(u"ゲンガーズのそのポケモンはまだ捕獲されていません")
                    return False
        else:
            logging.error(u"ポケモン名が不正で、DBから正しく取得できません")
            return False
    else:
        logging.error(u"ポケモン名がブランクです")


def getAllSortedByNormalOrder():
    """
    変数はとらない
    返却型はPokemonListのリスト型
    """
    return PokemonList.query().order(PokemonList.normalOrder).fetch()


def getSortedByTime(number, team):
    """
    変数はとってくるデータの数とチーム名
    返却型はPokemonListのリスト型
    """
    if team == u'ピクシーズ':
        return PokemonList.query().order(-PokemonList.clefableTime).fetch(number)
    elif team == u'ゲンガーズ':
        return PokemonList.query().order(-PokemonList.gengarTime).fetch(number)
    else:
        logging.fatal(u'チーム名が不正です。')
        return None


def getSortedByRecentGet(number):
    """
    変数はとってくるデータの数
    返却型はPokemonListのリスト型
    """
    clefable = PokemonList.query().order(-PokemonList.clefableTime).fetch(number)
    gengar = PokemonList.query().order(-PokemonList.gengarTime).fetch(number)
    
    c = 0
    g = 0
    val = []
        
    for i in range(number):
        if clefable[c].clefableFlag or gengar[g].gengarFlag:
            if clefable[c].clefableTime >= gengar[g].gengarTime:
                clefable[c] = copy.copy(clefable[c])
                clefable[c].clefableViewFlag = True
                clefable[c].gengarViewFlag = False
                val.append(clefable[c])
                c += 1
            else:
                gengar[g] = copy.copy(gengar[g])
                gengar[g].gengarViewFlag = True
                gengar[g].clefableViewFlag = False
                val.append(gengar[g])
                g += 1
            
    return val



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


GENGARS_ORDER = (
15,
76,
108,
36,
80,
110,
43,
147,
77,
51,
60,
133,
70,
33,
131,
83,
4,
72,
6,
38,
66,
39,
16,
96,
1,
54,
67,
58,
97,
105,
57,
98,
126,
135,
91,
52,
140,
130,
85,
42,
7,
95,
99,
32,
103,
109,
68,
111,
146,
25,
134,
30,
127,
5,
93,
64,
150,
63,
148,
138,
44,
100,
86,
116,
48,
145,
122,
120,
124,
18,
84,
10,
65,
92,
139,
90,
142,
8,
112,
3,
40,
41,
101,
61,
26,
11,
23,
87,
82,
78,
137,
114,
34,
27,
35,
69,
121,
56,
117,
115,
107,
13,
81,
12,
14,
118,
119,
132,
28,
75,
74,
22,
37,
143,
88,
62,
53,
45,
59,
55,
123,
106,
50,
29,
19,
49,
71,
141,
73,
89,
102,
113,
17,
31,
9,
47,
24,
94,
136,
21,
104,
125,
20,
149,
79,
46,
144,
128,
2,
129)


NICO_TIMES = (
8826,
9155,
20361,
451,
7194,
7948,
101,
1747,
5767,
7375,
8060,
9572,
780,
12441,
12515,
1367,
11195,
21019,
12996,
15773,
1477,
9217,
6824,
18951,
10870,
11473,
20472,
20682,
9288,
6195,
12265,
6242,
6351,
7041,
8270,
8526,
8379,
8464,
20292,
21060,
1670,
18109,
9436,
15868,
15889,
1637,
17924,
9395,
14673,
6645,
6756,
13492,
17288,
13262,
16176,
8647,
13437,
14911,
15932,
12958,
19686,
19890,
19616,
17806,
20527,
14317,
20165,
20203,
8324,
8485,
8505,
16343,
16387,
14513,
14250,
20583,
11633,
16120,
15156,
13808,
10916,
18058,
3548,
7782,
18244,
15280,
15392,
21101,
20909,
15037,
15463,
5541,
7304,
7343,
14398,
6909,
17863,
13223,
13872,
10956,
12153,
6174,
6999,
7084,
14568,
9169,
20964,
15587,
11562,
11784,
6451,
18336,
18455,
11406,
6399,
15084,
19105,
12912,
14043,
15205,
15481,
19964,
19623,
20034,
11061,
20853,
13382,
8213,
1508,
16016,
10024,
14150,
4336,
13547,
7492,
4956,
20799,
12315,
20417,
20236,
20662,
12275,
5977,
16287,
11020,
20744,
7248,
7444,
17521,
18740)