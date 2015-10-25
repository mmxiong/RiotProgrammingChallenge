from constants import *
from api_key import API_KEY
import json
import os
import data_manager
import command_assembler

__author__ = 'Michael'

# TODO: create mapping from champion id to name
class SetUp:
    @staticmethod
    def get_champion_index():

        # if the index already exists, read from cached file
        # assume champion index is already up to date, don't need to cache
        if os.path.isfile('%s%s' % (CACHE_DIR, CHAMPION_INDEX_CACHE)):
            champion_index_file = '%s%s' % (CACHE_DIR, CHAMPION_INDEX_CACHE)
            champion_index = data_manager.DataManager.read_cached_data(champion_index_file)

        # else should download fresh from API
        else:
            index_url = command_assembler.CommandAssembler.assemble_command(0, PREFIX, API_KEY, REGION)
            champion_index = data_manager.DataManager.read_api_call(index_url)

            # if should cache, then write to champion index cache
            if CACHE:
                os.mkdir('%s' % CACHE_DIR)
                champion_index_file = open('%s%s' % (CACHE_DIR, CHAMPION_INDEX_CACHE), 'w')
                champion_index_file.write(json.dumps(champion_index))
                champion_index_file.close()

        return champion_index

# This code may be used for getting individual champions
"""
# if champion list is cached, read from file
    if os.path.isfile('&s&s' % (CACHE_DIR, CHAMPION_LIST_CACHE)):
        for champion in champion_index['champions']:
            champion_id = champion['id']
            champion_list_file = '%s%s' % (CACHE_DIR, CHAMPION_INDEX_CACHE)
            champion_list = data_manager.DataManager.read_cached_data(champion_list_fileham)


    else:
        for champion in champion_index['champions']:
            champion_id = champion['id']
            champion_url = command_assembler.CommandAssembler.assemble_command(1, PREFIX, API_KEY, REGION, champion_id)
            champion_json_list.append(data_manager.DataManager.read_api_call(champion_url))

    return champion_json_list
"""
