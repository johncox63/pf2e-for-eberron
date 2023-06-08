import re

def replace_compendium_references(input_string):
    # The pattern captures two parts: everything up to the last brace and the desired output.
    # These parts are separated by a pair of parentheses, creating a capture group.
    pattern = r'@Compendium\[.*?\]\{(.*?)\}'
    # The re.sub function replaces every match of the pattern with the contents of the first capture group.
    return re.sub(pattern, r'\1', input_string)

input_string = 'choose @Compendium[pf2e.spells-srd.gpzpAAAJ1Lza2JVl]{Detect Magic} or @Compendium[pf2e.spells-srd.lg73SvJZno1ypPAj]{Read the Air}.'
print(replace_compendium_references(input_string))