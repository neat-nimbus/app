#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
詳細ページに表示する情報をDBから取ってくる機能を持ちます
"""

import Dao.pokemonListDao

class ShowDetailModel:
    def show(self):
        """
        変数を取らず、detailViewInfoオブジェクトを返します
        """
        detailViewInfo = Dao.pokemonListDao.getAllSortedByNormalOrder()
        return detailViewInfo