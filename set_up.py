from constants import *
import json
import os
import data_manager
import command_assembler

__author__ = 'Michael'


# TODO: add documentation after deciding design of SetUp
"""
"""
class SetUp:

    """
    Returns a json object of champion data. Each key/value pair in data is keyed by
    champion_key (usually name, differences with occurrances of ' character such as
    Vel'Koz). Value contains name, id, key, and title of champion.
    """
    @staticmethod
    def get_champion_index():

        # if the index already exists, read from cached file
        # assume champion index is already up to date, don't need to cache
        # if unsure, clear cache and rerun
        if os.path.isfile('%s%s' % (CACHE_DIR, CHAMPION_INDEX_CACHE)):
            champion_index_file = '%s%s' % (CACHE_DIR, CHAMPION_INDEX_CACHE)
            champion_index = data_manager.DataManager.read_cached_data(champion_index_file)

        # else should download fresh from API
        else:
            index_url = command_assembler.CommandAssembler.assemble_command(0, PREFIX, API_KEY, REGION)
            champion_index = data_manager.DataManager.read_api_call(index_url)

            # if should cache, then write to champion index cache
            if CACHE:
                os.makedirs('%s' % CACHE_DIR, exist_ok=True)
                champion_index_cache_file = open('%s%s' % (CACHE_DIR, CHAMPION_INDEX_CACHE), 'w')
                champion_index_cache_file.write(json.dumps(champion_index))
                champion_index_cache_file.close()

        return champion_index['data']
