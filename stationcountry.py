import csv

import pycountry_convert as pc

d = {}
f = open("venv/station_country_data.dat", "r")
for x in f:
    d[(x.split(",")[0]).replace('"', '')] = (x.split(",")[1].replace('"', '').replace('\n', '').title())
f.close()


def country_to_continent(country_name):
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name
    except:
        pass

countrySet = set()

with open('venv\stationid.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Country", "Continent"])
    for k, v in d.items():
        if (country_to_continent(v) == 'Asia' or country_to_continent(v) == 'Africa'):
            if (not v in countrySet):
                countrySet.add(v)
                writer.writerow([k ,v, country_to_continent(v)])
f.close()
