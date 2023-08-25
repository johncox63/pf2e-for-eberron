import os
import json

def combine_json_files_in_directory(directory):
    combined_data = {
        "customPackID": "",
        "customPackName": "",
        "listCustomSpecial": []
    }

    # Step 1: Get all files in the directory
    all_files = os.listdir(directory)

    # Step 2: Filter only for .json files
    json_files = [f for f in all_files if f.endswith('.json')]

    # Step 3: Loop through and read each .json file
    for file in json_files:
        file_path = os.path.join(directory, file)
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

            # Copy the customPackID and customPackName from the first file only
            if not combined_data["customPackID"]:
                combined_data["customPackID"] = data["customPackID"]
                combined_data["customPackName"] = data["customPackName"]

            combined_data["listCustomSpecial"].extend(data["listCustomSpecial"])

    return combined_data

def main():
    # Determine the directory from which the script is executed
    current_directory = os.path.dirname(os.path.realpath(__file__))
    marks_directory = os.path.join(current_directory, 'Marks')

    combined_data = combine_json_files_in_directory(marks_directory)

    # Step 4: Write the combined data to dragonmarks.json
    with open(os.path.join(current_directory, 'dragonmarks.json'), 'w') as output_file:
        json.dump(combined_data, output_file, indent=4)

if __name__ == "__main__":
    main()
