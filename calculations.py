__author__ = 'Michael'

"""
This class contains various methods for doing calculations relevant to finding the most efficient spell.
"""

class Calculations():

    # calculates total damage from a given base, ratios, and stats
    @staticmethod
    def calculate_damage(base, ratios, scaling_stats, ap, ad, bonus_ad):
        total = base

        for x in range(len(scaling_stats)):
            if 'spelldamage' in scaling_stats[x]:
                total += ratios[x] * ap
            elif 'attackdamage' in scaling_stats[x]:
                total += ratios[x] * ad
            elif 'bonusattackdamage' in scaling_stats[x]:
                total += ratios[x] * bonus_ad

        return total


    # converts health values to equivalent gold value
    # 2.67 is the ratio of gold to health provided by a ruby crystal
    # health potion arguably a better comparison, but there is no mana equivlanet in S6 (mana potions removed)
    # for the purposes of calculation, this results in a larger resulting "efficiency" value
    # however, relative efficiencies remain largely the same
    @staticmethod
    def convert_health_to_gold(health):
        return health * 2.67


    # same as above function for mana
    # uses 2:1 ratio of mana to gold provided by mana crystal
    @staticmethod
    def convert_mana_to_gold(mana):
        return mana * 2


    # uses formula:
    # [(gain in gold) - (cost in gold)]/cooldown
    # approximates gold per second efficiency of a spell
    @staticmethod
    def calculate_efficiency(gain, cost, cooldown):
        try:
            return (gain - cost) / cooldown
        except ZeroDivisionError:
            return gain - cost
