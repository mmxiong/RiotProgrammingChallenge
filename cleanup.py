import shutil
from constants import *

__author__ = 'Michael'


# This script cleans up all cached files created by the efficiency calculator
def clean_up_cache():
    shutil.rmtree(CACHE_DIR, ignore_errors=True)

if __name__ == '__main__':
    clean_up_cache()
