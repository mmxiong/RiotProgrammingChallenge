from constants import *
import set_up
import shutil

__author__ = 'Michael'


def main():
    # clean_up_cache()
    set_up.SetUp.get_champion_index()
    # TODO: count champions


# TODO: find a home for this function
def clean_up_cache():
    shutil.rmtree(CACHE_DIR)


if __name__ == '__main__':
    main()
