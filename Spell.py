__author__ = 'Michael'

"""
This class represents a spell, and has a parsing method (set_damage) that sets
damage, ratios, and scaling stats. Other values are set in constructor.
"""

class Spell:
    def __init__(self, spell_json):

        self.json = spell_json
        self.key = spell_json['key']
        self.damage = []
        self.ratios = []
        self.scaling_stats = []
        self.cost_type = spell_json['costType']
        self.cost = spell_json['cost'][-1]
        self.cooldown = spell_json['cooldown'][-1]

        self.set_damage()

    def set_damage(self):
        # if vars key is not in the json, then the spell must not scale on ap/ad
        # we ignore these, as their efficiencies may depend on other factors (eg. Mundo's Q)
        if 'vars' not in self.json or 'effect' not in self.json:
            # still need to set damage to a number (0)
            self.damage = sum(self.damage)
            return

        vars = self.json['vars']
        # scaling keys will hold a1, a2, f1, etc.
        # this allows us to parse the sanitizedTooltip for relevant base damages
        scaling_keys = []
        # if we find a key in sanitizedTooltip, we want to add the relevant ratio and stat to the self.ratios and
        # self.scaling_stats list
        # we don't add them immediatley when we find them because of cases like Ahri's Q (same base, same scaling, 2 ways)
        key_to_scaling = {}

        # goes through the vars array and pulls out each scaling factor of the spell
        # afterwards, scaling keys contains a bunch of scaling variables (a1, f2, etc.)
        for x in range(len(vars)):
            ratio = vars[x]['coeff']
            scaling_stat = vars[x]['link']
            key = vars[x]['key']

            if ratio is None or key is None or scaling_stat not in {'bonusattackdamage', 'attackdamage', 'spelldamage'}:
                continue

            key_to_scaling[key] = (scaling_stat, ratio)
            scaling_keys.append(key)

        sanitized_tooltip = self.json['sanitizedTooltip'].split()

        # holds damage keys (eg. e1, e2, etc.)
        damage_set = set()

        # parse sanitized tooltip for each scaling_key, and find the previous effect variable (e1, e2, etc.)
        for x in range(len(sanitized_tooltip)):
            if sanitized_tooltip[x] in scaling_keys:
                # if there is a closing paren, then there was another scaling variable before this one
                # happens in cases of scaling off both AD and AP
                if ')' in sanitized_tooltip[x-2] and self.is_damage(sanitized_tooltip[x-6]):
                    damage_set.add(x-6)
                # otherwise, this is the scaling key directly following the base damage 3 indexes back
                elif self.is_damage(sanitized_tooltip[x-3]):
                    damage_set.add(x-3)
                self.scaling_stats.append(key_to_scaling[sanitized_tooltip[x]][0])
                self.ratios.append(key_to_scaling[sanitized_tooltip[x]][1][-1])

        # once damage_set is populated, we replace those keys with actual damage values in the self.damage list
        for index in damage_set:
            # damage key should be of form e* where * is some int
            damage_key = sanitized_tooltip[index]
            # effects array holds damages
            effects = self.json['effect']
            damage_array = effects[int(damage_key[1])]
            # we add in the last element (base damage at max level)
            self.damage.append(damage_array[len(damage_array) - 1])

        self.damage = sum(self.damage)

    # simply returns whether or not a specific string is of the form e*
    # if it is, it represents a variable representing a base damage value
    def is_damage(self, some_str):
        return len(some_str) is 2 and some_str.startswith('e') and some_str[1].isnumeric()

    # for debugging purposes
    def print_info(self):
        print("key: %s" % self.key)
        print("damage: %s" % self.damage)
        print("scaling: %s" % self.ratios)
        print("scaling stat: %s" % self.scaling_stats)
        print("cost type: %s" % self.cost_type)
        print("cost: %s" % self.cost)
        print("cooldown: %s" % self.cooldown)
