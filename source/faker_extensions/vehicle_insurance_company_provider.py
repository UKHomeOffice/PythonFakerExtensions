import random

from faker import Faker
from faker.providers import BaseProvider

from faker_extensions.data import vehicle_insurance_company


class VehicleInsuranceCompanyProvider(BaseProvider):
    """ Provide Fake vehicle insurer based on real data"""

    def vehicle_insurance_company(self):
        return random.choice(vehicle_insurance_company.insurers)


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider - note the construction of a non instance
    fake.add_provider(VehicleInsuranceCompanyProvider(fake))
    # Use it!

    insurer = fake.vehicle_insurance_company()
    print(insurer)


if __name__ == '__main__':
    main()
