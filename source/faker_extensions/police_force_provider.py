from faker import Faker
from faker_extensions.abstract_providers import DictionaryProvider


class PoliceForceProvider(DictionaryProvider):
    """ Provide Fake police force from real data"""

    forces = [
        {'pncCode': 52, 'hoRadioCode': 'QP', 'force': 'Avon and Somerset Constabulary'},
        {'pncCode': 40, 'hoRadioCode': 'VA', 'force': 'Bedfordshire Police'},
        {'pncCode': 93, 'hoRadioCode': 'BX', 'force': 'British Transport Police'},
        {'pncCode': 35, 'hoRadioCode': 'VB', 'force': 'Cambridgeshire Constabulary'},
        {'pncCode': 84, 'hoRadioCode': 'AH', 'force': 'Police Scotland (formerly Central Scotland Police)'},
        {'pncCode': 7, 'hoRadioCode': 'BA', 'force': 'Cheshire Constabulary'},
        {'pncCode': 48, 'hoRadioCode': 'CP', 'force': 'City of London Police'},
        {'pncCode': 17, 'hoRadioCode': 'LZ', 'force': 'Cleveland Police'},
        {'pncCode': 3, 'hoRadioCode': 'BB', 'force': 'Cumbria Constabulary'},
        {'pncCode': 30, 'hoRadioCode': 'NA', 'force': 'Derbyshire Constabulary'},
        {'pncCode': 50, 'hoRadioCode': 'QB', 'force': 'Devon and Cornwall Constabulary'},
        {'pncCode': 55, 'hoRadioCode': 'QC', 'force': 'Dorset Police'},
        {'pncCode': 70, 'hoRadioCode': 'AJ', 'force': 'Police Scotland (formerly Dumfries & Galloway Constabulary)'},
        {'pncCode': 11, 'hoRadioCode': 'LA', 'force': 'Durham Constabulary'},
        {'pncCode': 63, 'hoRadioCode': 'WH', 'force': 'Heddlu Dyfed Powys Police'},
        {'pncCode': 42, 'hoRadioCode': 'VG', 'force': 'Essex Police'},
        {'pncCode': 78, 'hoRadioCode': 'ZT', 'force': 'Police Scotland (formerly Fife Constabulary)'},
        {'pncCode': 53, 'hoRadioCode': 'QL', 'force': 'Gloucestershire Constabulary'},
        {'pncCode': 82, 'hoRadioCode': 'UB', 'force': 'Police Scotland (formerly Grampian Police)'},
        {'pncCode': 6, 'hoRadioCode': 'CK', 'force': 'Greater Manchester Police'},
        {'pncCode': 61, 'hoRadioCode': 'WO', 'force': 'Heddlu Gwent Police'},
        {'pncCode': 44, 'hoRadioCode': 'HC', 'force': 'Hampshire Constabulary'},
        {'pncCode': 41, 'hoRadioCode': 'VH', 'force': 'Hertfordshire Constabulary'},
        {'pncCode': 16, 'hoRadioCode': 'XH', 'force': 'Humberside Police'},
        {'pncCode': 46, 'hoRadioCode': 'KA', 'force': 'Kent Police'},
        {'pncCode': 4, 'hoRadioCode': 'BD', 'force': 'Lancashire Constabulary'},
        {'pncCode': 33, 'hoRadioCode': 'NL', 'force': 'Leicestershire Constabulary'},
        {'pncCode': 32, 'hoRadioCode': 'NC', 'force': 'Lincolnshire Police'},
        {'pncCode': 76, 'hoRadioCode': 'ZH', 'force': 'Police Scotland (formerly Lothian & Borders Police)'},
        {'pncCode': 5, 'hoRadioCode': 'CH', 'force': 'Merseyside Police'},
        {'pncCode': 1, 'hoRadioCode': 'MP', 'force': 'Metropolitan Police (also 02)'},
        {'pncCode': None, 'hoRadioCode': 'GT', 'force': 'Metropolitan Police (special events)'},
        {'pncCode': 36, 'hoRadioCode': 'VK', 'force': 'Norfolk Constabulary'},
        {'pncCode': 34, 'hoRadioCode': 'NG', 'force': 'Northamptonshire Police'},
        {'pncCode': 10, 'hoRadioCode': 'LB', 'force': 'Northumbria Police'},
        {'pncCode': 12, 'hoRadioCode': 'XN', 'force': 'North Yorkshire Police'},
        {'pncCode': 60, 'hoRadioCode': 'WA', 'force': 'Heddlu North Wales Police'},
        {'pncCode': 31, 'hoRadioCode': 'NH', 'force': 'Nottinghamshire Police'},
        {'pncCode': 62, 'hoRadioCode': 'WL', 'force': 'Heddlu South Wales Police'},
        {'pncCode': 14, 'hoRadioCode': 'XS', 'force': 'South Yorkshire Police'},
        {'pncCode': 21, 'hoRadioCode': 'YF', 'force': 'Staffordshire Police'},
        {'pncCode': 74, 'hoRadioCode': 'AS', 'force': 'Police Scotland (formerly Strathclyde Police)'},
        {'pncCode': 37, 'hoRadioCode': 'VL', 'force': 'Suffolk Constabulary'},
        {'pncCode': 45, 'hoRadioCode': 'HJ', 'force': 'Surrey Police'},
        {'pncCode': 47, 'hoRadioCode': 'KB', 'force': 'Sussex Police'},
        {'pncCode': 80, 'hoRadioCode': 'ZS', 'force': 'Police Scotland (formerly Tayside Police)'},
        {'pncCode': 43, 'hoRadioCode': 'HB', 'force': 'Thames Valley Police'},
        {'pncCode': 23, 'hoRadioCode': 'YJ', 'force': 'Warwickshire Police'},
        {'pncCode': 22, 'hoRadioCode': 'YK', 'force': 'West Mercia Police'},
        {'pncCode': 20, 'hoRadioCode': 'YM', 'force': 'West Midlands Police'},
        {'pncCode': 13, 'hoRadioCode': 'XW', 'force': 'West Yorkshire Police'},
        {'pncCode': 54, 'hoRadioCode': 'QJ', 'force': 'Wiltshire Constabulary'}
    ]

    def __init__(self, generator):
        super().__init__(self.forces, generator)

    def force(self):
        return self.get_choice()


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider - note the construction of a non instance
    fake.add_provider(PoliceForceProvider(fake))
    # Use it!
    force = fake.force()
    print(force)


if __name__ == '__main__':
    main()
