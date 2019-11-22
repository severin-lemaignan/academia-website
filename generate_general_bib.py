#! /usr/bin/env python3

import json

with open('publications.json', encoding="utf-8") as data_file:
    data = json.load(data_file)
    for entry in data:
        if "bibtex" in entry:
            bibtex = "\n\t".join(entry["bibtex"].split('\\n'))
            print(bibtex)
