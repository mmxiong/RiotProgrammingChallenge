import setup
import spell
from constants import *
from calculations import *
import os.path

__author__ = 'Michael'

"""
This is the main efficiency calculator. Running this program as main will allow the user to input various values of
AP, AD, bonus AD, and CDR. These parameters affect the calculations of ability efficiency. The program will then
calculate the efficiency of all spells in the game and print the spell with the highest efficiency. Efficiency
is defined as [(gain converted to gold) - (cost converted to gold)]/cooldown. Conversions to gold are done using the
ratio of health/mana gained per gold of a ruby/mana crystal.
"""


def main():

    # set cdr, ap, ad, and bonus ad values
    cdr = ""
    ap = ""
    ad = ""
    bonus_ad = ""

    while not ap.isnumeric():
        ap = input("Ability Power: ")

    while not ad.isnumeric():
        ad = input("Total Attack Damage: ")

    while not bonus_ad.isnumeric():
        bonus_ad = input("Bonus Attack Damage: ")

    while not cdr.isnumeric():
        cdr = input("Cooldown Reduction (%): ")

    cdr = float(cdr)/100
    ap = int(ap)
    ad = int(ad)
    bonus_ad = int(bonus_ad)

    if not os.path.isdir(CACHE_DIR):
        print("Caching champion index for future use...")
        setup.cache_champion_index()

    if not os.path.isdir("%s/%s" % (CACHE_DIR, SPELL_CACHE_DIR)):
        print("Caching champion spells for future use...")
        setup.cache_champion_spells()


    # get champion index in order to iterate over every champion
    champion_index = setup.get_champion_index()

    efficiencies = []

    most_efficient_spell_champion = ""
    most_efficient_spell_number = -1
    most_efficient_spell_efficiency = 0
    most_efficient_spell_key = ""

    for entry in champion_index:

        # array of champion spells
        champion_spells = setup.get_champion_spells(entry)

        # for each spell in the array (transform champions have more than 4)
        for x in range(len(champion_spells)):
            # some champion spells should be ignored (see README)
            if champion_spells[x]['key'] in ignore_spells:
                continue

            # spell object holds relevant variables
            champion_spell = spell.Spell(champion_spells[x])

            # get stats from spell object
            base = champion_spell.damage
            cost = champion_spell.cost
            cost_type = champion_spell.cost_type
            ratios = champion_spell.ratios
            scaling_stats = champion_spell.scaling_stats
            cooldown = champion_spell.cooldown * (1 - cdr)

            # some spells don't do damage, heal, or shield (eg. Akali w)
            # we don't care about them
            if base is 0:
                continue

            # convert stats to gold for comparison
            total_damage = Calculations.calculate_damage(base, ratios, scaling_stats, ap, ad, bonus_ad)
            total_damage_gold = Calculations.convert_health_to_gold(total_damage)

            if 'Mana' in cost_type:
                cost_gold = Calculations.convert_mana_to_gold(cost)
            elif 'Health' in cost_type:
                cost_gold = Calculations.convert_health_to_gold(cost)
            elif 'Energy' in cost_type:
                cost_gold = cost
            # various non-mana, health, or energy costs
            elif 'NoCost' in cost_type \
                    or 'none' in cost_type \
                    or 'Heat' in cost_type\
                    or 'Passive' in cost_type\
                    or 'Builds1Ferocity' in cost_type:
                cost_gold = 0
            else:
                cost_gold = 0

            # calculate efficiency
            efficiency = Calculations.calculate_efficiency(total_damage_gold, cost_gold, cooldown)

            if efficiency > most_efficient_spell_efficiency:
                most_efficient_spell_champion = entry
                most_efficient_spell_key = champion_spell.key
                most_efficient_spell_efficiency = efficiency
                most_efficient_spell_number = x + 1

    if most_efficient_spell_number is 1:
        spell_key = 'Q'
    elif most_efficient_spell_number is 2:
        spell_key = 'W'
    elif most_efficient_spell_number is 3:
        spell_key = 'E'
    else:
        spell_key = 'R'

    print("The most efficient spell with given inputs is: %s's %s with key: %s"
          % (most_efficient_spell_champion, spell_key, most_efficient_spell_key))

if __name__ == '__main__':
    main()
