import random
from datetime import date
from enum import Enum
from random import randint

import rstr
from dateutil.relativedelta import relativedelta
from faker import Faker
from faker.providers import BaseProvider

from faker_extensions.data import financial_institutions


class CardTypes(Enum):

    def __init__(self, value, full_name, code):
        self._value_ = value
        self.full_name = full_name
        self.code = code

    AMERICAN_EXPRESS = (1, 'American Express', 'AX')
    BANK_CARD = (2, 'Bank Card', 'BC')
    CARTE_BLEU = (3, 'Carte Bleu', 'BL')
    CARTE_BLANCHE = (4, 'Carte Blanche', 'CB')
    DINERS_CLUB = (5, 'Diners Club', 'DN')
    DISCOVER_CARD = (6, 'Discover Card', 'DS')
    EUROCARD = (7, 'Eurocard', 'EC')
    JAPANESES_CREDIT_BUREAU = (8, 'Japanese Credit Bureau Credit Card', 'JC')
    MAESTRO = (9, 'Maestro', 'MA')
    MASTER_CARD = (10, 'Master Card', 'MC')
    SOLO = (11, 'Solo', 'SO')
    UNION_PAY = (12, 'Union Pay', 'CU')
    UNIVERSAL_AIR_TRAVEL_CARD = (13, 'Universal Air Travel Card', 'TP')
    VISA_ELECTRON = (14, 'Visa Electron', 'VE')
    VISA = (15, 'Visa', 'VI')


class FinanceCardProvider(BaseProvider):
    card_regex = "[0-9]{4}[0-9]{4}[0-9]{4}[0-9]{4}"
    list_cards = list(CardTypes.__iter__())

    def number(self):
        return rstr.xeger(self.card_regex)

    def issuer(self):
        return random.choice(list(financial_institutions.financial_institutions.keys()))

    def expiry_date(self, today):
        """returns a date +- 3 years from now"""
        three_years_ago = today + relativedelta(years=-3)
        three_years_in_the_future = today + relativedelta(years=+3)

        return date.fromordinal(random.randint(three_years_ago.toordinal(),
                                               three_years_in_the_future.toordinal()))

    def type(self):
        return random.choice(self.list_cards)

    def finance_card(self):
        expiry_date = self.expiry_date(date.today())
        start_date = expiry_date + relativedelta(years=-4)
        typ = self.type()
        return {
            "number": self.number(),
            "expiry_month": expiry_date.month,
            "expiry_year": expiry_date.year,
            "expiry_date": expiry_date,
            "start_date": start_date,
            "start_year": start_date.year,
            "start_month": start_date.month,
            "issuer": self.issuer(),
            "type": typ.full_name,
            "code": typ.code
        }


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(FinanceCardProvider)

    number = fake.number()
    print(number)

    issuer = fake.issuer()
    print(issuer)

    expiry_date = fake.expiry_date(date.today())
    print(expiry_date)

    type = fake.type()
    print(type)

    finance_card = fake.finance_card()
    print(finance_card)


if __name__ == '__main__':
    main()
