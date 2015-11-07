Riot Programming Challenge

Language: Python 3

To run:
Run analyze.py
To clean up:
Run cleanup.py

This program calculates the most efficient spell in League of Legends given different amounts of AP, AD,
bonus AD, and CDR. It does so by making API calls to the Riot API in order to get all data on the 127
champions, and their spells. This data is cached for subsequent executions of the program, and can be
cleaned by running the cleanup.py file.

The program calculates efficiency by converting gains and costs of the spell to gold and then dividing
the resulting value by the cooldown.

Efficiency = [(gain in gold) - (cost in gold)]/cooldown

I chose to do use this model as it provided an even playing field with which to compare gains and costs.
The resulting efficiency value is a measure of value in gold per second. In other words, each second, using
a particular spell will provide the user x amount of gold value. Although an imperfect model, it was a
fairly clean way to compare apples and oranges. In doing so, I made a few assumptions.

Assumptions:

1. Damage = Healing = Shielding
damage on an enemy = shielding or healing on an ally

2. Ignore CC:
Spells like Taric's Dazzle have crowd control effects attached to them. Without a more robust model, it was
not possible to account for the value brought to the table by cc effects. Therefore, they were ignored, and
only damage/shielding/healing values were taken into account as "gains".

3. Ignore inaccurate values in the API
Some champions had inaccuracies in the data provided by the API. For example, Ezreal's Q scales .4 off of AP
and 1.1 off of AD. However, his 1.1 ratio on AD was not reflected in the API. In these cases, the behavior of
the program is undefined. Sometimes, the spell is simply skipped, other times, the spell is assumed to not have
the specific scaling. Also of note is the fact that some champions like Lux had no BASE damages (Lux's E).
The same remains true; behavior in these cases is undefined.

4. Other special cases
Some spells are charge based, rather than cooldown based (Akali's Shadow Dance). These abilities feature
extremely low cooldowns that skewed the calculations. There was not an easy way in order to extract charge
generation times to be used as replacement cooldowns. For this reason, spells like these were skipped. A full
list of spells that were skipped can be found in the constants.py file. The ignore_spells set contains the
keys of the spells to be skipped.


Documentation:

api_key:
IMPORTANT: In order to run the program, a file called api_key.py must be created with the following line of code:
API_KEY = <API KEY>
where <API KEY> is replaced by one's own API key. Mine is omitted for privacy.

analyze:
This file contains main for the efficiency calculator. Run this in order to calculate ability efficiencies.

calculations:
This file contains the Calculations class which contains various methods used in calculating ability efficiencies.

    Class: Calculations
        Method: calculate_damage(base, ratios, scaling_stats, ap, ad, bonus_ad)
            Input: base damage, scaling stats, scaling ratios, and relevant stats
            Output: Total Damage

        Method(s): convert_health_to_gold(health), convert_mana_to_gold(mana):
            Input: Health or Mana
            Output: Equivalent gold value

        Method: calculate_efficiency(gain, cost, cooldown):
            Input: Gain and cost in gold, cooldown:
            Output: Efficiency

data_manager:
Contains DataManager object. It takes a URL or file name and returns the resulting json.

    Class: ApiManager
        Method: read_api_call(url)
            Input: URL
            Output: JSON of returned data

        Method: read_cached_data(filename)
            Input: File Path
            Output: JSON of returned data

command_assembler:
Contains CommandAssembler object. It takes in a command code, prefix, api_key, and optionally
region and champion_id. These arguments specify a specific command to be assembled for use
with the Riot API.

    Class: CommandAssembler
        Method: assemble_command(command, prefix, api_key,
                                 region=None, champion_id=None)
            Input: parameters for API call
            Output: URL

setup:
Library of 4 functions for getting champion data.

    Function: cache_champion_index()
        Input: Nothing
        Output: Nothing -- /cache/ directory is created with champion_index.txt which contains
            a JSON of basic information about every champion

    Function: cache_champion_spells()
        Input: Nothing
        Output: Nothing -- /cache/spells/ directory containing <champion_key>_spells.txt for
            each champion which contains a JSON array of 4 elements (one for each spell).

    Function: get_champion_index()
        Input: Nothing
        Output: Returns the champion index cached by cahce_champion_index() in JSON form

    Function: get_champion_spells(key)
        Input: Champion key
        Output: Returns the spells of the champion specified in JSON form

spell:
Object representing a spell. Contains JSON describing spell, and various relevant variables extracted from the JSON

    Class: Spell
        Method: __init__(spell_json)
            Input: JSON format object of the spell
            Output: Simply sets relevant variables for future access

        Method: set_damage()
            Input: Nothing
            Output: Sets self.damage, self.ratios, and self.scaling_stats

        Method: is_damage()
            Input: some string
            Output: True if string is a damage key, False otherwise

        Method: print_info()
            Input: Nothing
            Output: Prints the spell (for debugging purposes)


