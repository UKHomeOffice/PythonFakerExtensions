from datetime import date
from unittest import TestCase

from faker_extensions.nationality_provider import NationalityProvider


class TestNationalityProvider(TestCase):

    def test_uk_national_by_birth_birth_generate_dates(self):
        # given
        country_of_birth = NationalityProvider.countries_by_iso2['GB']['country_or_area']
        dob = date(1960, 10, 10)
        today = date(2020, 5, 13)

        # when
        result = NationalityProvider.generate_nationality_dates(country_of_birth, True, dob, today)

        self.assertNotIn('dateOfArrival', result)
        self.assertNotIn('dateOfNationalisation', result)

    def test_uk_nationality_attained_after_birth_generate_dates(self):
        # given
        country_of_birth = NationalityProvider.countries_by_iso2['IN']['country_or_area']
        dob = date(1960, 10, 10)
        today = date(2020, 5, 13)

        # when
        result = NationalityProvider.generate_nationality_dates(country_of_birth, True, dob, today)

        # then
        self.assertGreaterEqual(result['dateOfArrival'], dob)
        self.assertGreaterEqual(result['dateOfNationalisation'], result['dateOfArrival'])

    def test_uk_non_uk_national_generate_dates(self):
        # given
        country_of_birth = NationalityProvider.countries_by_iso2['AU']['country_or_area']
        dob = date(1960, 10, 10)
        today = date(2020, 5, 13)

        # when
        result = NationalityProvider.generate_nationality_dates(country_of_birth, False, dob, today)

        # then
        self.assertGreaterEqual(result['dateOfArrival'], dob)
        self.assertNotIn('dateOfNationalisation', result)
