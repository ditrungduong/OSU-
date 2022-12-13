# Author: Ditrung Duong
# GitHub username: ditrungduong
# Date: 10/17/2022
# Description: A class that read a data source and a method to search for winner surname using year and category

import json


class NobelData:
    """Representing a Nobel data source """

    def __init__(self):
        """Reading nobel data source"""
        self._nobel_info = open('nobels.json', 'r')

    def search_nobel(self, year, category):
        """returns a sorted list of the surnames for the winner(s) in that category for that year."""
        result = []
        with self._nobel_info as infile_data_source:
            nobel_data = json.load(infile_data_source)
            for data in nobel_data['prizes']:
                if year == data['year'] and category == data['category']:
                    for winner in data['laureates']:
                        result.append(winner['surname'])

        result.sort()
        return result

