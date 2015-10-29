import setup

__author__ = 'Michael'

"""
This class represents a champion for the purposes of analyzing spells. It contains fields
key, champion_id, champion_name, and champion_spells. Upon init, it takes a key and the
champion_index json and sets the aforementioned fields. It also features accessors for
each field.

"""
class Champion:
    def __init__(self, key):
        champion_index = setup.get_champion_index()
        # takes in champion key, reads from index to get name, id, and spells
        self.champion_key = key
        self.champion_id = champion_index[key]['id']
        self.champion_name = champion_index[key]['name']
        self.champion_spells = setup.get_champion_spells(key)

