#!/usr/bin/env python
# coding:UTF-8
"""
ビューは必ず、メソッドの返却型を辞書型にする必要があります
"""


class PokemonView():
    def __init__(self, updateInfo):
        self.pokemon = updateInfo.pokemon
        self.team = updateInfo.team

    def getValues(self):
	self.pokemon.encode('utf_8')
	self.team.encode('utf_8')
        return {'getPokemon':self.pokemon, 'getTeam':self.team}