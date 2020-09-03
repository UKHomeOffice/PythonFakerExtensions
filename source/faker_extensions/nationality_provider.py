import random
from datetime import date

from faker import Faker
from faker.providers import BaseProvider

from faker_extensions.data import country_data


class NationalityProvider(BaseProvider):
    asylum_options = ['pending', 'refused', 'withdrawn', 'granted']

    countries_by_name = country_data.countries_by_name()
    countries_by_iso2 = country_data.countries_by_iso2_code()

    GB = countries_by_iso2['GB']['country_or_area']

    def nationality(self, country_of_birth, dob):
        # generate and add nationality details
        # 58% of the non-UK born population also hold British Nationality
        is_british_national = random.randrange(100) < 58 or country_of_birth == \
                              NationalityProvider.countries_by_iso2['GB']['country_or_area']

        attributes = NationalityProvider.generate_nationality_dates(country_of_birth, is_british_national, dob,
                                                                    date.today())

        if is_british_national:  # if the person is a british national, set their nationality to GBR
            attributes['nationality'] = \
                NationalityProvider.countries_by_iso2['GB']
        else:  # else assume it is the country of birth
            attributes['nationality'] = \
                NationalityProvider.countries_by_name[country_of_birth]

        # 6% of immigrants are seeking asylum
        if not is_british_national and random.randrange(100) < 58:
            attributes['asylumStatus'] = random.choice(NationalityProvider.asylum_options)

        return attributes

    @staticmethod
    def generate_nationality_dates(country_of_birth, is_british_national, dob, today):
        attributes = {}

        if country_of_birth != NationalityProvider.countries_by_iso2['GB']['country_or_area']:
            date_of_arrival = date.fromordinal(random.randint(dob.toordinal(), today.toordinal()))
            attributes['dateOfArrival'] = date_of_arrival
            if is_british_national:  # if the person has attained British nationality after birth
                attributes['dateOfNationalisation'] = \
                    date.fromordinal(random.randint(date_of_arrival.toordinal(), today.toordinal()))

        return attributes


def main():
    """Runs the provider. The test file has more specific cases."""
    fake = Faker(['en_UK'])
    fake.add_provider(NationalityProvider)

    number = fake.nationality(NationalityProvider.countries_by_iso2['GB']['country_or_area'], date(1960, 10, 10))
    print(number)

    number = fake.nationality(NationalityProvider.countries_by_iso2['IN']['country_or_area'], date(1960, 10, 10))
    print(number)


if __name__ == '__main__':
    main()
