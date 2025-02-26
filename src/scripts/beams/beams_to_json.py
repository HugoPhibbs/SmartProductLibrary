import os
import json
import ifcopenshell.file
from src.core.LibraryObject import LibraryObject

# Script to convert all IFC files in the single beams directory to JSON files

OBJECTS_DIR = r"C:\Users\hugop\Documents\Work\SmartObjectLibrary\data\objects"

if __name__ == "__main__":

    single_beams_ifc_dir = os.path.join(OBJECTS_DIR, "ifc")

    json_dir = os.path.join(OBJECTS_DIR, "json")

    if not os.path.exists(json_dir):
        os.makedirs(json_dir)

    for i, file in enumerate(os.listdir(single_beams_ifc_dir)):
        file_path = os.path.join(single_beams_ifc_dir, file)
        ifc_file = ifcopenshell.open(file_path)
        object, _ = LibraryObject.from_ifc_file(ifc_file)

        object_dict = object.to_dict()

        with open(os.path.join(json_dir, f"{object.id}.json"), "w") as json_file:
            json.dump(object_dict, json_file, indent=4)