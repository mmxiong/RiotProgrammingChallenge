from constants import *
import os
import json
import data_manager
import command_assembler

__author__ = 'Michael'

"""
This class represents a champion for the purposes of analyzing spells. It contains fields
key, champion_id, champion_name, and champion_spells. Upon init, it takes a key and the
champion_index json and sets the aforementioned fields. It also features accessors for
each field.

"""
class Champion:
    def __init__(self, key, champion_index):
        # takes in champion key, reads from index to get name, id, and spells
        self.champion_key = key
        self.champion_id = champion_index[key]['id']
        self.champion_name = champion_index[key]['name']
        self.champion_spells = self.read_champion_spells()

    # returns champion_spells as json array
    def read_champion_spells(self):
        # if champion is cached, read from champion file
        # assume champion is up to date, don't need to API call
        # if unsure, clear cache and rerun
        if os.path.isfile('%s%s%s%s' % (CACHE_DIR, SPELL_CACHE_DIR, self.champion_key, CHAMPION_SPELL_CACHE)):
            champion_spell_file = ('%s%s%s%s' % (CACHE_DIR, SPELL_CACHE_DIR, self.champion_key, CHAMPION_SPELL_CACHE))
            champion_spells = data_manager.DataManager.read_cached_data(champion_spell_file)
        # else make new API call
        else:
            champion_spell_url = command_assembler.CommandAssembler.assemble_command\
                (1, PREFIX, API_KEY, REGION, self.champion_id, 'spells')
            champion_spells = data_manager.DataManager.read_api_call(champion_spell_url)['spells']

            # if should cache, then write to champion spell cache file
            if CACHE:
                os.makedirs('%s%s' % (CACHE_DIR, SPELL_CACHE_DIR), exist_ok=True)
                champion_spell_cache_file = open('%s%s%s%s' % (CACHE_DIR, SPELL_CACHE_DIR, self.champion_key, CHAMPION_SPELL_CACHE) , 'w')
                champion_spell_cache_file.write(json.dumps(self.champion_spells))
                champion_spell_cache_file.close()

        return champion_spells
    # returns champion key as a string
    def get_key(self):
        return self.champion_key

    # returns champion name as a string
    def get_name(self):
        return self.champion_name

    # returns champion id as an int
    def get_id(self):
        return self.champion_id

    # returns spells as json array
    def get_spells(self):
        return self.champion_spells
