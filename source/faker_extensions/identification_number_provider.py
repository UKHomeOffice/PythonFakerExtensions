""" Provides a UK faker_extensions.identification number, alongside its issue and expiration date """

from datetime import date
from enum import Enum

import rstr
from faker import Faker
from faker.providers import BaseProvider

from faker_extensions.identification.uk_national_insurance_generator import UkNationalInsuranceNumberGenerator
from faker_extensions.identification.uk_provisional_driving_licence_generator import UkProvisionalDrivingLicenceGenerator
from faker_extensions.identification.uk_full_driving_licence_generator import UkFullDrivingLicenceGenerator
from faker_extensions.identification.uk_passport_generator import UkPassportGenerator


class Identity(Enum):
    """ Types of identity """

    def __init__(self, value, identity_form):
        self._value_ = value
        self.identity_form = identity_form

    UK_PASSPORT = (1, 'UK Passport')
    UK_FULL_DRIVING_LICENCE = (2, 'Full UK Driving Licence')
    UK_PROVISIONAL_DRIVING_LICENCE = (3, 'Provisional UK Driving Licence')
    UK_NATIONAL_INSURANCE_NUMBER = (4, 'National Insurance Number')


class IdentificationNumberProvider(BaseProvider):
    """ Provides a UK faker_extensions.identification number, alongside its issue and expiration date """

    identity_forms = {
        Identity.UK_PASSPORT: UkPassportGenerator(),
        Identity.UK_FULL_DRIVING_LICENCE: UkFullDrivingLicenceGenerator(),
        Identity.UK_PROVISIONAL_DRIVING_LICENCE: UkProvisionalDrivingLicenceGenerator(),
        Identity.UK_NATIONAL_INSURANCE_NUMBER: UkNationalInsuranceNumberGenerator()
    }

    def generate_id_code_for_identity_form(self, id_form):
        """ Generates a random id based on the regex for the id form """
        return rstr.xeger(id_form.regex)

    def identification_number(self, dob, id_form_name):
        id_form = self.identity_forms[id_form_name]
        issue_date = id_form.generate_issue_date(dob, date.today())

        return {"id_form": id_form_name.name,
                "id_number": self.generate_id_code_for_identity_form(id_form),
                "id_issue_date": issue_date,
                "id_expiry_date": id_form.generate_expiration_date(issue_date, dob)
                }


def main():
    dob = date(1970, 1, 1)
    fake = Faker(['en_UK'])
    fake.add_provider(IdentificationNumberProvider(fake))

    generated_id = fake.identification_number(dob, Identity.UK_FULL_DRIVING_LICENCE)
    print(generated_id)

    generated_id = fake.identification_number(dob, Identity.UK_PROVISIONAL_DRIVING_LICENCE)
    print(generated_id)

    generated_id = fake.identification_number(dob, Identity.UK_PASSPORT)
    print(generated_id)

    generated_id = fake.identification_number(dob, Identity.UK_NATIONAL_INSURANCE_NUMBER)
    print(generated_id)


if __name__ == '__main__':
    main()
