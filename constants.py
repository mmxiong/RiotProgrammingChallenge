__author__ = 'Michael'

from api_key import *

# CONFIG OPTIONS
PREFIX = 'https://na.api.pvp.net'
REGION = 'na'
CACHE_DIR = 'cache/'
CHAMPION_INDEX_CACHE = 'champion_index_cache.txt'
SPELL_CACHE_DIR = 'spells/'
CHAMPION_SPELL_CACHE = '_spells.txt'

ignore_spells = {
    'XerathArcaneBarrage2',
    'YasuoDashWrapper',
    'VelkozW',
    'HeimerdingerQ',
    'SyndraW',
    'SorakaW',
    'RumbleGrenade',
    'RengarE',
    'RengarW',
    'AatroxW',
    'TeemoRCast',
    'ShyvanaTransformCast',
    'YasuoRKnockUpComboW',
    'AkaliShadowDance',
    'KhazixQ',
    'KarthusDefile',
    'ViE',
    'VorpalSpikes'
}