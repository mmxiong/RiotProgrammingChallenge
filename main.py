from constants import *
import set_up
import shutil
import champion

__author__ = 'Michael'


def main():
    #clean_up_cache()
    champion_index = set_up.SetUp.get_champion_index()

    # champ is key name
    for entry in champion_index:
        champ = champion.Champion(entry, champion_index)

# TODO: find a home for this function
def clean_up_cache():
    shutil.rmtree(CACHE_DIR, ignore_errors=True)


if __name__ == '__main__':
    main()
