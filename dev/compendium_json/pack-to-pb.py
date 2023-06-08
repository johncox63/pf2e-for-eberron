import json
import os
import re

def replace_compendium_references(input_string):
    # The pattern captures two parts: everything up to the last brace and the desired output.
    # These parts are separated by a pair of parentheses, creating a capture group.
    pattern = r'@Compendium\[.*?\]\{(.*?)\}'
    # The re.sub function replaces every match of the pattern with the contents of the first capture group.
    return re.sub(pattern, r'\1', input_string)

BASE_DIR = os.getcwd()
# Read the JSON file
file_path= BASE_DIR + '/dev/compendium_json/pf2e-for-eberron.pf2e-for-eberron-spells.json'

with open(file_path, 'r') as file:
    data = json.load(file)

# Select elements to query and create a new list with the desired format
output_data = []
for item in data:
    # Extract selected elements
    name = item['name']
    spell_type = item['system']['spellType']['value']
    category = item['system']['category']['value']
    level = item['system']['level']['value']
    target = item['system']['target']['value']
    duration = item['system']['duration']['value']
    range = item['system']['range']['value']
    save = item['system']['save']['value']
    actions = item['system']['time']['value']
    description = item['system']['description']['value']
    traits = item['system']['traits']['value']
    school = item['system']['school']['value']
    area = ''
    if item['system']['area'] is not None:
        area_num = item['system']['area']['value']
        area_type = item['system']['area']['type']
        area = str(area_num)+" "+area_type
    cast_focus = item['system']['components']['focus']
    cast_material = item['system']['components']['material']
    cast_somatic = item['system']['components']['somatic']
    cast_verbal = item['system']['components']['verbal']

    cast = ''
    if cast_focus == True:
        cast = 'focus, '
    if cast_material == True:
        cast = cast+'material, '
    if cast_somatic == True:
        cast = cast+'somatic, '
    if cast_verbal == True:
        cast = cast+'verbal, '
    cast = cast[:-2]

    description = replace_compendium_references(description)

    # Consolidate traits into a comma-delimited string
    traits_str = ', '.join(traits)
    traits_str = traits_str.replace("hb_","")
    traits_str = traits_str.replace("-"," ")
    # Create a dictionary with the desired format
    if category == 'focus':
        output_item = {
                "id": "",
                "name": name,
                "type": category,
                "traits": traits_str+", "+school+", 3rd Party",
                "actions": actions,
                "cast": cast,
                "description": description,
                "src": "PF2E for Eberron",
                "level": level,
                "databaseID": 1,
                "timestamp": "1686136458228",
                "target": target,
                "duration": duration,
                "range": range,
                "save": save,
                "area": area
        }

        # Add the item to the output list
        output_data.append(output_item)
out_path= BASE_DIR + '/pathbuilder/pf2e-for-eberron-spells.json'
# Write the output data to a new JSON file
with open(out_path, 'w') as file:
    json.dump(output_data, file, indent=4)
