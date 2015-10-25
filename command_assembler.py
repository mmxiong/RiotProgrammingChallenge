__author__ = 'Michael'

"""
This class features static methods that can be used to assemble commands used to access
the Riot API. Only assemble_command should be called, which is a switching method that
calls the corresponding assembler method for the command given. Options are put into a
dictionary for the specific assembler method to use.
"""


class CommandAssembler:
    @staticmethod
    def assemble_command(command, prefix, api_key,
                         region=None, champion_id=None):

        # TODO: check if api_key is none, then return error

        api_key_suffix = '?api_key=%s' % api_key
        # create dictionary with information
        options = dict(prefix=prefix,
                       region=region,
                       champion_id=champion_id,
                       api_key=api_key_suffix)

        return switcher[command](options)

    @staticmethod
    def assemble_get_champion_index(options):
        return '%s/api/lol/static-data/%s/v1.2/champion%s' \
               % (options['prefix'],
                  options['region'],
                  options['api_key'])

    @staticmethod
    def assemble_get_champion_by_id(options):
        return '%s/api/lol/static-data/%s/v1.2/champion/%s%s' \
               % (options['prefix'],
                  options['region'],
                  options['champion_id'],
                  options['api_key'])

switcher = {
    0: CommandAssembler.assemble_get_champion_index,
    1: CommandAssembler.assemble_get_champion_by_id
}
