import uuid
import json
import os
from copy import deepcopy

def process_master_marks(input_file, dragonmark_name):
    with open(input_file, 'r') as file:
        data = json.load(file)

    for item in data['listCustomSpecial']:
        item['id'] = str(uuid.uuid4())
        item['name'] = item['name'].replace('DRAGONMARKREPLACE', dragonmark_name)
        item['description'] = item['description'].replace('DRAGONMARKREPLACE', dragonmark_name)
    return data

def get_bonus_amount(mark_item):
    return 1 if mark_item['level'] in [1, 17] or "Evolution Spell 2" in mark_item['name'] else 0

def update_master_spells(master_spells_file, master_marks_data, spells_to_include):
    with open(master_spells_file, 'r') as file:
        master_spells_data = json.load(file)

    updated_items = []
    
    for spell_item in master_spells_data['listCustomSpecial']:
        # Check if the spell name contains any string from spells_to_include
        if any(substring in spell_item['name'] for substring in spells_to_include):
            for mark_item in master_marks_data['listCustomSpecial']:
                spell_item_copy = deepcopy(spell_item)  # Deep copy the spell item

                spell_item_copy['id'] = str(uuid.uuid4())  # Set a unique UUID
                spell_item_copy['parentID'] = mark_item['id']
                spell_item_copy['level'] = mark_item['level']

                # Update bonusAmount
                bonus_amount = get_bonus_amount(mark_item)
                for effect in spell_item_copy['listCustomEffects']:
                    effect['bonusAmount'] = bonus_amount
                
                updated_items.append(spell_item_copy)

    master_spells_data['listCustomSpecial'] = updated_items
    return master_spells_data

def save_to_file(data, output_filename):
    with open(output_filename, 'w') as file:
        json.dump(data, file, indent=4)

dragonmark_name = "Aberrant"
current_path = os.path.dirname(os.path.abspath(__file__))

spells_to_include = [
    "Dragonmarked Guidance",
    "Warded Resilience",
    "Warder's Intuition",
    "Pushing Gust",
    "Storm's Riposte",
    "Cantrip of the Guard",
    "Dragonmarked Warder",
    "Guard and Seal",
    "Personal Blizzard",
    "Spell Guard",
    "Summon Living Dragonmark",
    "Siberys' Reconstruction"
]

# Process MasterMarks.json
master_marks_file = os.path.join(current_path, "MasterMarks.json")
master_marks_data = process_master_marks(master_marks_file, dragonmark_name)

# Update MasterSpells.json
master_spells_file = os.path.join(current_path, "MasterSpells.json")
master_spells_data = update_master_spells(master_spells_file, master_marks_data, spells_to_include)

# Save the processed master_marks_data to {dragonmark_name}.json
master_marks_output = os.path.join(current_path, f"{dragonmark_name}.json")
save_to_file(master_marks_data, master_marks_output)
# Save updated master_spells_data
master_spells_output = os.path.join(current_path, f"{dragonmark_name}_Spells.json")
save_to_file(master_spells_data, master_spells_output)