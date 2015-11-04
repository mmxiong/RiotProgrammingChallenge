from constants import *
from calculations import *
import setup
import champion
import spell

__author__ = 'Michael'

log_file = 'log.txt'

def main():

    log = open(log_file, 'w')

    ap = 0
    ad = 0
    bonus_ad = 0
    cdr = 0


    champion_index = setup.get_champion_index()
    champion_index_list = []
    for entry in champion_index:
        champion_index_list.append(entry)

    champion_index_list.sort()

    efficiencies = []

    for entry in champion_index_list:

        print(entry)
        # if entry in ['Leona', 'Heimerdinger', 'MissFortune', 'Gnar']:
        #     continue

        champ = champion.Champion(entry)

        for x in range(3):
            champion_spell = spell.Spell(champ.champion_spells[x])

            # get stats from spell object
            base = 100 # champion_spell.damage
            cost = champion_spell.cost
            cost_type = champion_spell.cost_type
            ratios = []# champion_spell.scaling
            scaling_stats = [] # champion_spell.scaling_stat
            cooldown = 10 # champion_spell.cooldown * (1 - cdr)

            # convert stats to gold for comparison
            total_damage = calculate_damage(base, ratios, scaling_stats, ap, ad, bonus_ad)
            total_damage_gold = convert_health_to_gold(total_damage)

            if cost_type is 'Mana':
                cost_gold = convert_mana_to_gold(cost)
            elif cost_type is 'Health':
                cost_gold = convert_health_to_gold(cost)
            else:
                cost_gold = 0
                log.write("%s's spell: %s has unknown cost: %s" % (entry, champion_spell.key, cost_type))

            efficiency = calculate_efficiency(total_damage_gold, cost_gold, cooldown)

            efficiencies.append(str(efficiency ) + str(champion_spell.key))

    efficiencies.sort()
    print(efficiencies)

    log.close()

if __name__ == '__main__':
    main()
