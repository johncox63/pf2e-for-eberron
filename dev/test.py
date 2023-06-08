import json
import os

from constants import *

for compendium_item in COMPENDIUM_ITEM_LIST:
    file_path= BASE_DIR + '\packs\\' + PACK_NAME + '-' + compendium_item +'.db'
    print(compendium_item + ' - Step 1')

    json_str = '['
    json_count = 0
    try:
        with open(file_path, 'r') as json_file:
            for json_line in json_file:
                try:
                    json_count += 1
                    line = json_line.replace("\n",",").strip()
                    json_str = json_str+line

                except ValueError:
                    pass
    except:
        pass
    
    if json_str[len(json_str)-1] == ',':
        json_str = json_str[:-1]

    json_str = json_str+']'

    print(compendium_item + ' - Step 2')

    with open('dev\compendium_json\\'+PACK_NAME+'.'+PACK_NAME+'-'+compendium_item+'.json',"w") as out_file:
        out_file.write(json_str)

    print(compendium_item + ' - Step 2b')

    json_object = json.loads(json_str)
 
    #with open('dev\compendium_json\\'+PACK_NAME+'.'+PACK_NAME+'-'+compendium_item+'.json',"w") as out_file:
    #    out_file.write('')

    #for json_item in json_object:
    #    print(json_item['name'], ";", json_item['_id'],';',json_item['flags']['core']['sourceId'])
    #    json_item['flags']['core']['sourceId'] = PACK_NAME+'.'+PACK_NAME+'-'+compendium_item+'.'+json_item['_id']
    #    json_item['system']['source']['value'] = 'PF2E for Eberron'
    #    print(json.dumps(json_item))
    
    print(compendium_item + ' - Step 3')

    json_formatted_str = json.dumps(json_object,indent=2)

    with open('dev\compendium_json\\'+PACK_NAME+'.'+PACK_NAME+'-'+compendium_item+'.json',"w") as out_file:
        out_file.write(json_formatted_str)

    print(compendium_item + ' - Step 4')