__author__ = 'Michael'

"""
This class represents a spell, and has a parsing method (set_attributes) that sets
relevant variables.
"""

class Spell:
    def __init__(self, spell_json):

        self.json = spell_json
        self.key = ""
        self.damage = []  # get damage
        self.scaling = []  # get scaling
        self.scaling_stat = []  # get scaling stat
        self.damage_type = []  # get damage type
        self.cost_type = ""
        self.cost = 0
        self.cooldown = 0

        self.set_attributes()

    def set_attributes(self):

        sanitized_tooltip = self.json['sanitizedTooltip'].split()

        damage_var = []
        scaling_var = []

        for x in range(len(sanitized_tooltip)):

            if sanitized_tooltip[x].lower().startswith(('magic', 'physical', 'true')):
                y = x
                self.damage_type.append(sanitized_tooltip[x])
                while not sanitized_tooltip[y].startswith('{{'):
                    if sanitized_tooltip[y].startswith('a'):
                        scaling_var.append(sanitized_tooltip[y])

                    if sanitized_tooltip[y].startswith('e'):
                        damage_var.append(sanitized_tooltip[y][1])

                    y -= 1

        for each in damage_var:
            self.damage.append(self.json['effect'][int(each)])

        for each in scaling_var:
            vars = self.json['vars']

            for var in vars:
                if var['key'].startswith(each):
                    self.scaling.append(var['coeff'])
                    self.scaling_stat.append(var['link'])

        self.cost_type = self.json['costType']
        self.cost = self.json['cost']
        self.cooldown = self.json['cooldown']
        self.key = self.json['key']

    def print_info(self):
        print("key: %s" % self.key)
        print("damage: %s" % self.damage)
        print("scaling: %s" % self.scaling)
        print("scaling stat: %s" % self.scaling_stat)
        print("damage type: %s" % self.damage_type)
        print("cost type: %s" % self.cost_type)
        print("cost: %s" % self.cost)
        print("cooldown: %s" % self.cooldown)
