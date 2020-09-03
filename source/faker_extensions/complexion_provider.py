import random
from faker import Faker
from faker.providers import BaseProvider

complexion = [
    "pale",
    "tanned",
    "unshaven",
    "beard",
    "pock marked",
]


class ComplexionProvider(BaseProvider):
    """ Provide Fake (simple) colour. Example of categorical"""

    # noinspection PyMethodMayBeStatic
    def complexion(self):
        return random.choice(complexion)


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider
    fake.add_provider(ComplexionProvider)
    # Use it!
    chosen_complexion = fake.complexion()
    print(chosen_complexion)


if __name__ == '__main__':
    main()
