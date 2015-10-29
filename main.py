from constants import *
import setup
import shutil
import champion
import spell

__author__ = 'Michael'


def main():
    # for now I'm assuming my cache is already done properly (it is)
    # just going to analyze Ahri (mostly damaging spells)

    # ahri = champion.Champion('Ahri')

    # ahri_q = spell.Spell(ahri.champion_spells[0])
    # ahri_q.print_info()

    # ahri_w = spell.Spell(ahri.champion_spells[1])
    # ahri_w.print_info()

    # ahri_e = spell.Spell(ahri.champion_spells[2])
    # ahri_e.print_info()

    aatrox = champion.Champion('Aatrox')

    # aatrox_q = spell.Spell(aatrox.champion_spells[0])
    # aatrox_q.print_info()

    # aatrox_w = spell.Spell(aatrox.champion_spells[1])
    # aatrox_w.print_info()

    aatrox_e = spell.Spell(aatrox.champion_spells[2])
    aatrox_e.print_info()

# TODO: find a home for this function
def clean_up_cache():
    shutil.rmtree(CACHE_DIR, ignore_errors=True)

if __name__ == '__main__':
    main()
