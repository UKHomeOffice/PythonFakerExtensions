from faker import Faker

from faker_extensions.abstract_providers import WeightedProvider
from faker_extensions.data import hobbies


class HobbyProvider(WeightedProvider):

    def __init__(self, generator):
        super().__init__(hobbies.hobby_distributions, generator)

    def hobby(self):
        return self.get_choice()


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(HobbyProvider(fake))

    hobby = fake.hobby()
    print(hobby)
    print(hobby.name_value())


if __name__ == '__main__':
    main()
