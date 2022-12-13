# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 10/17/2022
# Description: Adding, removing pet as well as wring pet info and load pet info

import json


class DuplicateNameError(Exception):
    """User defined exception for adding duplicate pet in the list"""
    pass


class NeighborhoodPets:
    """Representing neighborhood pet"""

    def __init__(self):
        self._name = None
        self._species = None
        self._owner_name = None
        self._pet_dict = {}

    def add_pet(self, pet_name, pet_species, pet_owner):
        """Adding pet to pet dict"""
        if pet_name in self._pet_dict:
            raise DuplicateNameError
        else:
            self._pet_dict[pet_name] = [pet_species, pet_owner]

    def delete_pet(self, pet_names):
        """Deleting pet out of pet dict"""
        if pet_names in self._pet_dict:
            del self._pet_dict[pet_names]

    def get_owner(self, pet_name):
        """Return name of the owner using pet name"""
        return self._pet_dict[pet_name][1]

    def save_as_json(self, file_name):
        """Take name of file and save as json"""
        with open(file_name, 'w') as outfile:
            outfile.write(json.dumps(self._pet_dict))

    def read_json(self, file_name):
        """Open json file using input name"""
        with open(file_name, 'r') as infile:
            self._pet_dict = json.load(infile)

    def get_all_species(self):
        """Return all species of pet"""
        species_list = set()
        for name in self._pet_dict:
            species_list.add(self._pet_dict[name][0])
        return species_list



