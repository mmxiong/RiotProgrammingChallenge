import setup
import spell

__author__ = 'Michael'


def main():

    champion_index = setup.get_champion_index()
    champion_index_list = []
    for entry in champion_index:
        champion_index_list.append(entry)

    champion_index_list.sort()

    for entry in champion_index_list:
        champion_spells = setup.get_champion_spells(entry)

        for x in range(len(champion_spells)):
            print('%s spell #%s' % (entry, x + 1))
            champ_spell = spell.Spell(champion_spells[x])
            champ_spell.print_info()
            print('\n')

if __name__ == '__main__':
    main()
