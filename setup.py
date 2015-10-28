from constants import *
import json
import os
import data_manager
import command_assembler

__author__ = 'Michael'


# TODO: add documentation after deciding design of SetUp

"""
Library for setting up the cached files for future use.
"""


def cache_champion_index():

    # if the index doesn't already exist, need to get and cache data
    if not os.path.isfile('%s%s' % (CACHE_DIR, CHAMPION_INDEX_CACHE)):
        index_url = command_assembler.CommandAssembler.assemble_command(0, PREFIX, API_KEY, REGION)
        champion_index = data_manager.DataManager.read_api_call(index_url)

        os.makedirs('%s' % CACHE_DIR, exist_ok=True)
        champion_index_cache_file = open('%s%s' % (CACHE_DIR, CHAMPION_INDEX_CACHE), 'w')
        champion_index_cache_file.write(json.dumps(champion_index))
        champion_index_cache_file.close()


def cache_champion_spells():
    champion_index = get_champion_index()
    for entry in champion_index:
        champion_id = champion_index[entry]['id']
        if not os.path.isfile('%s%s%s%s' % (CACHE_DIR, SPELL_CACHE_DIR, entry, CHAMPION_SPELL_CACHE)):
            champion_spell_url = command_assembler.CommandAssembler.assemble_command\
                (1, PREFIX, API_KEY, REGION, champion_id, 'spells')
            champion_spells = data_manager.DataManager.read_api_call(champion_spell_url)['spells']

            os.makedirs('%s%s' % (CACHE_DIR, SPELL_CACHE_DIR), exist_ok=True)
            champion_spell_cache_file = open('%s%s%s%s' % (CACHE_DIR, SPELL_CACHE_DIR, entry, CHAMPION_SPELL_CACHE) , 'w')
            champion_spell_cache_file.write(json.dumps(champion_spells))
            champion_spell_cache_file.close()


def get_champion_index():
    champion_index_file = ('%s%s' % (CACHE_DIR, CHAMPION_INDEX_CACHE))
    champion_index = data_manager.DataManager.read_cached_data(champion_index_file)
    return champion_index['data']


def get_champion_spells(key):
    champion_spell_file = ('%s%s%s%s' % (CACHE_DIR, SPELL_CACHE_DIR, key, CHAMPION_SPELL_CACHE))
    champion_spells = data_manager.DataManager.read_cached_data(champion_spell_file)
    return champion_spells
