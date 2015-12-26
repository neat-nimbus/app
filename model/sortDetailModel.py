#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
詳細ページに表示する情報をDBから取ってくる機能を持ちます
"""

import Dao.pokemonListDao
import logging

class SortDetailModel:
    def sortBy(self, detailViewInfo, sortMode):
        """
        チーム名を変数にとり、detailViewInfoオブジェクトを返します
        """
        if sortMode == u'ピクシーズ':
            detailViewInfo.sort(key=lambda x:x.clefableTime)
            detailViewInfo.sort(key=lambda x:x.clefableFlag, reverse=True)
        elif sortMode == u'ゲンガーズ':
            detailViewInfo.sort(key=lambda x:x.gengarOrder)
        elif sortMode == u'図鑑順':
            detailViewInfo.sort(key=lambda x:x.normalOrder)
        elif sortMode == u'ニコ動':
            detailViewInfo.sort(key=lambda x:x.nicoTime)
        else:
            logging.fatal(u"不正なソートキーです")
        return detailViewInfo
