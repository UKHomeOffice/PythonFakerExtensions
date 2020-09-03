from faker import Faker
from faker.providers.address.en_GB import Provider

from faker_extensions.abstract_providers import DictionaryProvider
from faker_extensions.data.addresses import addresses


class UKAddressProvider(DictionaryProvider):
    """ Provide Fake address based on real data"""

    def __init__(self, generator):
        super().__init__(addresses, generator)

    def address(self):
        return self.get_choice()


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider
    fake.add_provider(UKAddressProvider)
    # Use it!
    address = fake.address()
    print(address)


if __name__ == '__main__':
    main()
