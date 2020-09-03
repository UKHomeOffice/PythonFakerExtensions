import random

from faker import Faker
from faker.providers import BaseProvider

from faker_extensions.common_categories import Gender


class BuildProvider(BaseProvider):
    """ Provide build."""

    # noinspection PyMethodMayBeStatic
    def build(self, bmi, height, gender):
        return self.get_description_for_height_and_gender(height, gender) + ", " + random.choice(
            self.get_description_for_bmi(bmi))

    @staticmethod
    def get_description_for_height_and_gender(height, gender):
        """Returns a textual description of a person's height assuming:

            The average male is 178cm,
            The average female is 163cm

            Arbitrarily, 2.5% below average is short and 2.5% above is tall

            There may be a better to way to classify this
        """
        # 10% above and below median was chosen arbitrarily
        if gender is Gender.MALE:
            if height > 182.45:
                return "tall"
            elif height < 173.55:
                return "short"
            else:
                return "average height"
        elif gender is Gender.FEMALE:
            if height > 167.075:
                return "tall"
            elif height < 158.925:
                return "short"
            else:
                return "average height"

    @staticmethod
    def get_description_for_bmi(bmi):
        """Returns a list of possible textual descriptions of a person's bmi"""
        if bmi >= 30:
            return [
                "very overweight",
            ]
        elif bmi >= 25:
            return [
                "heavy",
            ]
        elif bmi >= 18.5:
            return [
                "slim",
                "average",
            ]
        else:
            return [
                "skinny",
                "thin",
            ]


def main():
    # How to create your own provider
    # Note you cannot have multiple locales!!!!
    fake = Faker(['en_UK'])
    # Add your provider
    fake.add_provider(BuildProvider)

    # Use it!
    build = fake.build(18.4, 163, Gender.FEMALE)
    print(build)

    # Use it!
    build = fake.build(20, 163, Gender.MALE)
    print(build)


if __name__ == '__main__':
    main()
