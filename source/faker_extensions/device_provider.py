import random

from faker import Faker

from faker_extensions.abstract_providers import WeightedProvider
from faker_extensions.data import devices


class DeviceProvider(WeightedProvider):

    def __init__(self, generator):
        super().__init__(devices.device_manufacturer_distributions, generator)

    def device(self):
        # get a weighted random phone manufacturer
        manufacturer = self.get_choice()

        # get a random phone for the manufacturer
        model = random.choice(devices.enum_to_manufacturer[manufacturer])

        return {'manufacturer': manufacturer, 'model': model}


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(DeviceProvider(fake))

    device = fake.device()
    print(device['manufacturer'].name_value())
    print(device['model'].value)


if __name__ == '__main__':
    main()
