from faker import Faker
from faker.providers import BaseProvider
import rstr


class VehicleInsurancePolicyNumberProvider(BaseProvider):
    # Based on AVIVA format
    regex = "[0-9]{3}[A-Z]{9}"

    def policy_number(self):
        return rstr.xeger(self.regex)


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(VehicleInsurancePolicyNumberProvider)

    policy_number = fake.policy_number()
    print(policy_number)


if __name__ == '__main__':
    main()
