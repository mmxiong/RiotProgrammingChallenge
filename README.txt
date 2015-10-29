TODO: update documentation
Documentation:

data_manager:
Contains DataManager object. It takes a URL or file name and returns the resulting json.

    Class: ApiManager
        Method: read_api_call(url)
            Input: URL
            Output: JSON of returned data

        Method: read_cached_data(filename)
            Input: File Path
            Output: JSON of returned data

command_assembler:
Contains CommandAssembler object. It takes in a command code, prefix, api_key, and optionally
region and champion_id. These arguments specify a specific command to be assembled for use
with the Riot API.

    Class: CommandAssembler
        Method: assemble_command(command, prefix, api_key,
                                 region=None, champion_id=None)
            Input: parameters for API call
            Output: URL

setup:
Library of 4 functions for getting champion data.

    Function: cache_champion_index()
        Input: Nothing
        Output: Nothing -- /cache/ directory is created with champion_index.txt which contains
            a JSON of basic information about every champion

    Function: cache_champion_spells()
        Input: Nothing
        Output: Nothing -- /cache/spells/ directory containing <champion_key>_spells.txt for
            each champion which contains a JSON array of 4 elements (one for each spell).

    Function: get_champion_index()
        Input: Nothing
        Output: Returns the champion index cached by cahce_champion_index() in JSON form

    Function: get_champion_spells(key)
        Input: Champion key
        Output: Returns the spells of the champion specified in JSON form

champion.py:
Contains Champion object, which represents all data of a champion needed, including key,
name, id, and spells. Uses setup to fill out its data about champions.

    Function: __init__(key) (constructor)
        Input: Champion key
        Output: Nothing -- just sets class variables appropriately
