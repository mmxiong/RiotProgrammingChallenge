__author__ = 'Michael'


def calculate_damage(base, ratios, scaling_stats, ap, ad, bonus_ad):
    if len(scaling_stats) is not len(ratios):
        return 0

    total = base

    for x in range(len(scaling_stats)):
        if scaling_stats[x] is 'spelldamage':
            total += ratios[x] * ap
        elif scaling_stats[x] is 'attackdamage':
            total += ratios[x] * ad
        elif scaling_stats[x] is 'bonusattackdamage':
            total += ratios[x] * bonus_ad

    return total

# NOTE: I thought about using health and mana potion restore/cost ratios, but S6 sees the removal of mana pots, and a
# change in the cost of health pots

def convert_health_to_gold(health):
    return health * 2.67


def convert_mana_to_gold(mana):
    return mana * 2


def calculate_efficiency(gain, cost, cooldown):
    return (gain - cost)/cooldown
