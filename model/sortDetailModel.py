#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
詳細ページに表示する情報をDBから取ってくる機能を持ちます
"""

import Dao.pokemonListDao
import logging

class SortDetailModel:
    def sortByTime(self, detailViewInfo, team):
        """
        チーム名を変数にとり、detailViewInfoオブジェクトを返します
        """
        if team == u'ピクシーズ':
            detailViewInfo.sort(key=lambda x:x.clefableTime)
            detailViewInfo.sort(key=lambda x:x.clefableFlag, reverse=True)
        elif team == u'ゲンガーズ':
            detailViewInfo.sort(key=lambda x:x.gengarTime)
            detailViewInfo.sort(key=lambda x:x.gengarFlag, reverse=True)
        return detailViewInfo
    
    def sortByNormalOrder(self, detailViewInfo):
        """
        変数をとらず、detailViewInfoオブジェクトを返します
        """
        detailViewInfo.sort(key=lambda x:x.normalOrder)
        return detailViewInfo
