from faker import Faker
from faker_extensions.abstract_providers import DictionaryProvider
import faker_extensions.data.vehicles as vehicles


class VehicleProvider(DictionaryProvider):
    """ Provide Fake vehicle from real data. Note this currently uses a collection of over 6,000 vehicles
    scraped from ANPR data.  Its not an exhaustive list from manufacturers"""

    def __init__(self, generator):
        super().__init__(vehicles.vehicles, generator)

    def vehicle(self):
        return self.get_choice()


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider - note the construction of a non instance
    fake.add_provider(VehicleProvider(fake))
    # Use it!
    vehicle = fake.vehicle()
    print(vehicle)


if __name__ == '__main__':
    main()
