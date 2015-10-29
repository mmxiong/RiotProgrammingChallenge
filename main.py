from constants import *
import setup
import shutil
import champion
import spell

__author__ = 'Michael'


def main():
    # for now I'm assuming my cache is already done properly (it is)
    # just going to analyze Ahri (mostly damaging spells)

    ahri = champion.Champion('Ahri')
    # sanitized_tooltip = ahri.get_spells()[0]['sanitizedTooltip']
    #
    # some_string = ""
    # while sanitized_tooltip is not '':
    #     if sanitized_tooltip.startswith('{{'):
    #         while not sanitized_tooltip.startswith('}}'):
    #             some_string = some_string + sanitized_tooltip[0]
    #             sanitized_tooltip = sanitized_tooltip[1:]
    #         some_string = some_string + '}}'
    #         sanitized_tooltip = sanitized_tooltip[4:]
    #         if sanitized_tooltip.startswith('m'):
    #             print("magic damage")
    #         elif sanitized_tooltip.startswith('t'):
    #             print("true damage")
    #         print(some_string)
    #         some_string = ""
    #     sanitized_tooltip = sanitized_tooltip[1:]


    ahri_q = spell.Spell(ahri.champion_spells[0])


# TODO: find a home for this function
def clean_up_cache():
    shutil.rmtree(CACHE_DIR, ignore_errors=True)

if __name__ == '__main__':
    main()
