TODO: update documentation
Documentation:

data_manager:
Contains DataManager object. It takes a URL, and makes the call to the API, returning a JSON.
The URL should be created in the command_assembler file.

    Class: ApiManager
        Method: make_api_call(url)
            Input: URL
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