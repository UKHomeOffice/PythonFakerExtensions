import random
from string import ascii_uppercase

from faker import Faker
from faker.providers import BaseProvider
import rstr

from faker_extensions.data import financial_institutions

# map uppercase letters to numbers for check digit generation
UPPERCASE_LETTERS = {l: str(n) for l, n in zip(ascii_uppercase, range(10, 36))}


class FinanceAccountProvider(BaseProvider):
    sort_code_regex = "[0-9]{6}"
    account_number_regex = "[0-9]{8}"

    def sort_code_number(self):
        return rstr.xeger(self.sort_code_regex)

    def account_number(self):
        return rstr.xeger(self.account_number_regex)

    def financial_institution(self):
        return random.choice(list(financial_institutions.financial_institutions.keys()))

    def swift(self, financial_institution):
        bank_code = financial_institutions.financial_institutions[financial_institution]["bank_code"]
        return bank_code + "GB" + rstr.xeger("[0-9]{3}[A-Z]{2}")

    def iban(self, financial_institution, sort_code, account_number):
        bank_code = financial_institutions.financial_institutions[financial_institution]["bank_code"]
        bban = bank_code + sort_code + account_number
        check_digits = self.generate_check_digits(bban)

        return "GB" + check_digits + bban

    def generate_check_digits(self, bban):
        """Generates check digits for a bban, using the algorithm list at:
        http://iban.co.uk/generation.html
        """

        # invert the code to generate check digits
        iban_raw_inverted = bban + "GB00"
        iban_as_digits = ''.join(UPPERCASE_LETTERS[c] if c in UPPERCASE_LETTERS else c for c in iban_raw_inverted)

        remainder = int(iban_as_digits) % 97
        check = 98 - remainder

        return format(check, '02d')

    def finance_account(self):
        financial_institution = self.financial_institution()
        sort_code = self.sort_code_number()
        account_number = self.account_number()

        return {
            "financial_institution": financial_institution,
            "sort_code": sort_code,
            "account_number": account_number,
            "swift": self.swift(financial_institution),
            "iban": self.iban(financial_institution, sort_code, account_number)
        }


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(FinanceAccountProvider)

    sort_code = fake.sort_code_number()
    print(sort_code)

    account_number = fake.account_number()
    print(account_number)

    financial_institution = fake.financial_institution()
    print(financial_institution)

    iban = fake.iban(financial_institution, sort_code, account_number)
    print(iban)

    swift = fake.swift(financial_institution)
    print(swift)

    finance_account = fake.finance_account()
    print(finance_account)


if __name__ == '__main__':
    main()
