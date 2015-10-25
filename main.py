from constants import *
from api_key import API_KEY
import command_assembler
import api_manager

__author__ = 'Michael'



def main():
    get_champions()



    #print(api_manager.ApiManager.make_api_call(command_assembler.CommandAssembler.assemble_command(0, PREFIX, API_KEY, REGION)))
    #print(api_manager.ApiManager.make_api_call(command_assembler.CommandAssembler.assemble_command(1, PREFIX, API_KEY, REGION, 84)))

def get_champions():
    index_url = command_assembler.CommandAssembler.assemble_command(0, PREFIX, API_KEY, REGION)
    champion_index = api_manager.ApiManager.make_api_call(index_url)['champions']
    #for each champion in index
    for champion in champion_index:
        champion_id = champion['id']
        champion_url = command_assembler.CommandAssembler.assemble_command(1, PREFIX, API_KEY, REGION, champion_id)
        print(api_manager.ApiManager.make_api_call(champion_url))

    pass

if __name__ == '__main__':
    main()
