import json

from faker import Faker

import faker_extensions.data.country_data as country_data
import faker_extensions.data.language_data as language_data
from faker_extensions.abstract_providers import WeightedProvider


class CountryOfBirthProvider(WeightedProvider):
    """ Country of birth from real data"""

    cobs = {
        "GBR": 0.875184,
        "IND": 0.012026,
        "POL": 0.010887,
        "PAK": 0.008165,
        "IRL": 0.005981,
        "DEU": 0.0047,
        "BGD": 0.003608,
        "ZAF": 0.003497,
        "USA": 0.003117,
        "CHN": 0.003702,
        "NGA": 0.002927,
        "JAM": 0.002405,
        "FRA": 0.002374,
        "KEN": 0.002326,
        "ITA": 0.002279,
        "LTU": 0.002279,
        "ROU": 0.002152,
        "LKA": 0.002105,
        "PHL": 0.002073,
        "AUS": 0.001788,
        "PRT": 0.001741,
        "ZWE": 0.001741,
        "SOM": 0.00163,
        "GHA": 0.001551,
        "ESP": 0.001472,
        "CAN": 0.001329,
        "LVA": 0.001298,
        "TUR": 0.00125,
        "IRN": 0.001171,
        "HUN": 0.001123,
        "IRQ": 0.001108,
        "NPL": 0.00106,
        "NZL": 0.001013,
        "AFG": 0.000949,
        "MYS": 0.000934,
        "UGA": 0.000918,
        "NLD": 0.000902,
        "CYP": 0.001091,
        "BGR": 0.000839,
        "BRA": 0.000823,
        "SVK": 0.000823,
        "RUS": 0.000775,
        "CZE": 0.000712,
        "THA": 0.00068,
        "GRC": 0.000633,
        "MUS": 0.000617,
        "SGP": 0.000585,
        "JPN": 0.00057,
        "EGY": 0.000522,
        "MLT": 0.000491,
        "SAU": 0.000491,
        "COL": 0.000475,
        "TZA": 0.000475,
        "ZMB": 0.000475,
        "BEL": 0.000427,
        "SWE": 0.000427,
        "UKR": 0.000427,
        "VNM": 0.000427,
        "TTO": 0.000396,
        "CHE": 0.000364,
        "DZA": 0.000348,
        "KOR": 0.000348,
        "ERI": 0.000332,
        "DNK": 0.000316,
        "GUY": 0.000316,
        "XKK": 0.000316,
        "AUT": 0.000285,
        "COG": 9.5e-05,
        "ISR": 0.000285,
        "LBN": 0.000285,
        "NOR": 0.000285,
        "ALB": 0.000269,
        "MAR": 0.000269,
        "SLE": 0.000269,
        "YEM": 0.000269,
        "BRB": 0.000253,
        "MWI": 0.000253,
        "ETH": 0.000237,
        "AGO": 0.000222,
        "LBY": 0.000222,
        "CMR": 0.000206,
        "KWT": 0.00019,
        "ARE": 0.00019,
        "GMB": 0.000174,
        "GIB": 0.000174,
        "SYR": 0.000174,
        "BDI": 4.7e-05,
        "FIN": 0.000158,
        "ARG": 0.000142,
        "BIH": 0.000142,
        "MEX": 0.000142,
        "LCA": 0.000142,
        "IDN": 0.000127,
        "MOZ": 0.000127,
        "VCT": 0.000127,
        "BRN": 0.000111,
        "EST": 0.000111,
        "CIV": 0.000111,
        "VEN": 0.000111,
        "AZE": 9.5e-05,
        "BLR": 9.5e-05,
        "HRV": 9.5e-05,
        "JOR": 9.5e-05,
        "NAM": 9.5e-05,
        "PER": 9.5e-05,
        "SRB": 9.5e-05,
        "TUN": 9.5e-05,
        "BOL": 7.9e-05,
        "BWA": 7.9e-05,
        "ECU": 7.9e-05,
        "FJI": 7.9e-05,
        "GRD": 7.9e-05,
        "GTM": 7.9e-05,
        "LBR": 7.9e-05,
        "MDA": 7.9e-05,
        "RWA": 7.9e-05,
        "ATG": 6.3e-05,
        "BHR": 6.3e-05,
        "CHL": 6.3e-05,
        "DMA": 6.3e-05,
        "GIN": 6.3e-05,
        "KAZ": 6.3e-05,
        "MSR": 6.3e-05,
        "BMU": 4.7e-05,
        "CUB": 4.7e-05,
        "TLS": 4.7e-05,
        "OMN": 4.7e-05,
        "PNG": 4.7e-05,
        "SEN": 4.7e-05,
        "SVN": 4.7e-05,
        "KNA": 4.7e-05,
        "SWZ": 4.7e-05,
        "AIA": 3.2e-05,
        "BHS": 3.2e-05,
        "GEO": 3.2e-05,
        "GNB": 3.2e-05,
        "LAO": 3.2e-05,
        "LUX": 3.2e-05,
        "MKD": 3.2e-05,
        "MDG": 3.2e-05,
        "MNG": 3.2e-05,
        "MNE": 3.2e-05,
        "QAT": 3.2e-05,
        "SYC": 3.2e-05,
        "SHN": 3.2e-05,
        "SDN": 3.2e-05,
        "UZB": 3.2e-05,
        "ARM": 1.6e-05,
        "BLZ": 1.6e-05,
        "IOT": 1.6e-05,
        "CAF": 1.6e-05,
        "CRI": 1.6e-05,
        "DOM": 1.6e-05,
        "HND": 1.6e-05,
        "ISL": 1.6e-05,
        "KGZ": 1.6e-05,
        "NER": 1.6e-05,
        "PRK": 1.6e-05,
        "PRY": 1.6e-05,
        "STP": 1.6e-05,
        "URY": 1.6e-05
    }

    def __init__(self, generator):
        super().__init__(self.cobs, generator)
        self.countries = country_data.countries_by_iso3_code()

    def country_of_birth(self):
        return self.countries[self.get_choice()]


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider - note the construction of a non instance
    fake.add_provider(CountryOfBirthProvider(fake))
    languages = language_data.languages_by_alpha2_code()
    for i in range(1, 2000):
        cob = fake.country_of_birth()
        print(cob)
        print(list(map(languages.get, cob['language_codes'])))


if __name__ == '__main__':
    main()
