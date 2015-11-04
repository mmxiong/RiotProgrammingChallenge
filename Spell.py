__author__ = 'Michael'

"""
This class represents a spell, and has a parsing method (set_attributes) that sets
relevant variables.
"""

class Spell:
    def __init__(self, spell_json):

        self.json = spell_json
        self.key = spell_json['key']

        # these will be set w/ set damage
        self.damage = []  # get damage

        # not yet useful, just looking at damages
        self.scaling = []  # get scaling
        self.scaling_stat = []  # get scaling stat




        self.cost_type = spell_json['costType']
        self.cost = spell_json['cost'][-1]
        self.cooldown = spell_json['cooldown'][-1]

        self.set_damage()

    def set_damage(self):
        sanitized_tooltip = self.json['sanitizedTooltip'].split()

        tooltip_index = 0

        while tooltip_index < len(sanitized_tooltip):
            if sanitized_tooltip[tooltip_index].lower().startswith(('deal', 'take', 'taking')):
                #then we need to do some parsing for base damages
                damage = ""
                tooltip_index += 1
                should_append = False

                while tooltip_index < len(sanitized_tooltip) and not sanitized_tooltip[tooltip_index].startswith('}}'):
                    if self.is_damage(sanitized_tooltip[tooltip_index]):
                        damage = sanitized_tooltip[tooltip_index]
                        should_append = True
                    tooltip_index += 1

                    if tooltip_index < len(sanitized_tooltip) and sanitized_tooltip[tooltip_index].endswith('%'):
                        should_append = False

                tooltip_index += 1
                if should_append:
                    self.damage.append(damage)
            tooltip_index += 1


    def is_damage(self, some_str):
        return len(some_str) is 2 and some_str.startswith(('e')) and some_str[1].isnumeric()

    def print_info(self):
        # print("key: %s" % self.key)
        print("damage: %s" % self.damage)
        # print("scaling: %s" % self.scaling)
        # print("scaling stat: %s" % self.scaling_stat)
        # print("damage type: %s" % self.damage_type)
        # print("cost type: %s" % self.cost_type)
        # print("cost: %s" % self.cost)
        # print("cooldown: %s" % self.cooldown)


        """
        self.key = self.json['key']

        sanitized_tooltip = self.json['sanitizedTooltip'].split()

        damage_var = []
        scaling_var = []

        for x in range(len(sanitized_tooltip)):

            if sanitized_tooltip[x].lower().startswith(('magic', 'physical', 'true'))\
                    and sanitized_tooltip[x + 1].lower().startswith('damage'):
                y = x
                self.damage_type.append(sanitized_tooltip[x])

                in_parens = False

                while not sanitized_tooltip[y].startswith('{{'):
                    temp = sanitized_tooltip[y]
                    if ')' in sanitized_tooltip[y]:
                        in_parens = True

                    if sanitized_tooltip[y].startswith(('a', 'f')) and 'additional' not in sanitized_tooltip[y]:
                        scaling_var.append(sanitized_tooltip[y])

                    if sanitized_tooltip[y].startswith('e'):
                        damage_var.append(sanitized_tooltip[y][1])

                    if '(' in sanitized_tooltip[y] and not in_parens:
                        break


                    y -= 1

        for each in damage_var:
            self.damage.append(self.json['effect'][int(each)])

        for ratio in scaling_var:
            try:
                vars = self.json['vars']

                for var in vars:
                    if var['key'].startswith(ratio):
                        self.scaling.append(var['coeff'])
                        self.scaling_stat.append(var['link'])
            except KeyError:
                self.scaling.append(0)
                self.scaling_stat




        self.cost_type = self.json['costType']
        self.cost = self.json['cost']
        self.cooldown = self.json['cooldown']
        self.key = self.json['key']
        """