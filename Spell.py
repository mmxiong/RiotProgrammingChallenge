__author__ = 'Michael'

class Spell:
    def __init__(self, spell_json):

        self.json = spell_json
        self.damage = [] # get damage
        self.scaling = [] # get scaling
        self.scaling_stat = "" # get scaling stat
        self.damage_type = [] # get damage type
        self.cost_type = ""
        self.cost = 0
        self.cooldown = 0

        self.set_attributes()

    def set_attributes(self):

        sanitized_tooltip = self.json['sanitizedTooltip'].split()

        damage_var = []
        scaling_var = []

        for x in range(len(sanitized_tooltip)):

            if sanitized_tooltip[x].startswith('{{'):
                damage_var.append(sanitized_tooltip[x + 1][1])

                if sanitized_tooltip[x + 3].startswith('(+{{'):
                    scaling_var.append(sanitized_tooltip[x + 4][1])

                if sanitized_tooltip[x + 6].startswith(('magic', 'physical', 'true')):
                    self.damage_type.append(sanitized_tooltip[x + 6])

                x += 6

        self.damage = self.json['effect']

        print(damage_var)
        print(scaling_var)
        print(self.damage_type)

        self.cost_type = self.json['costType']
        self.cost = self.json['cost']
        self.cooldown = self.json['cooldown']
