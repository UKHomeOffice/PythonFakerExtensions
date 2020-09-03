from faker import Faker
from faker.providers import BaseProvider
import rstr


class MobileNumberProvider(BaseProvider):
    regex = "^\+?(44)?(0|7)\d{9,13}$"

    def mobile_number(self):
        return rstr.xeger(self.regex)


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(MobileNumberProvider)

    mobile_number = fake.mobile_number()
    print(mobile_number)


if __name__ == '__main__':
    main()
