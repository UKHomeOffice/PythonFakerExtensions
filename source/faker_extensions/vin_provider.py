from faker import Faker
from faker.providers import BaseProvider
import rstr


class VinProvider(BaseProvider):
    regex = "^([A-Z\d]{3})[A-Z]{2}\d{2}([A-Z\d]{1})([X\d]{1})([A-Z\d]{3})\d{5}$"

    def vin_number(self):
        return rstr.xeger(self.regex)


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(VinProvider)

    vin = fake.vin_number()
    print(vin)


if __name__ == '__main__':
    main()
