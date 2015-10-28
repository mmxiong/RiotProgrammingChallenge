from constants import *
import setup
import shutil
import champion

__author__ = 'Michael'


def main():

    # clean_up_cache()
    setup.cache_champion_index()
    setup.cache_champion_spells()

    champion_index = setup.get_champion_index()

    # champ is key name
    for entry in champion_index:
        champ = champion.Champion(entry, champion_index)

# TODO: find a home for this function
def clean_up_cache():
    shutil.rmtree(CACHE_DIR, ignore_errors=True)

if __name__ == '__main__':
    main()
