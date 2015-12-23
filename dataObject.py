#!/usr/bin/env python
# coding:UTF-8

"""
各データ格納用オブジェクトです。
このファイル自体はオブジェクトの入れ物を定義するだけで、
機能は持たせません。
"""

class UpdateInfo():
    """
    あるチームがポケモンを捕まえたり、
    そのポケモンを削除しようとするときに使う元オブジェクト
    """
    def __init__(self, pokemon, team, mode):
        self.pokemon = pokemon
        self.team = team
        self.mode = mode


class MainViewInfo():
    """
    メインページの初期表示に使う情報を格納したオブジェクト
    """
    def __init__(self, clefableNumber="", gengarNumber="", pokemonList=""):
        self.clefableNumber = clefableNumber
        self.gengarNumber = gengarNumber
        self.pokemonList = pokemonList
