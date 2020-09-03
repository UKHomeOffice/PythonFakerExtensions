from datetime import date
from unittest import TestCase

from faker_extensions.identification.uk_provisional_driving_licence_generator import \
    UkProvisionalDrivingLicenceGenerator


class TestUkProvisionalDrivingLicenceGenerator(TestCase):
    def setUp(self):
        self.provisional_licence_generator = UkProvisionalDrivingLicenceGenerator()

    def test_generate_expiration_date_person_under_60_at_issue(self):
        # Given
        issue_date = date(1999, 12, 31)
        dob = date(1940, 1, 1)

        # When
        expiration_date = self.provisional_licence_generator.generate_expiration_date(issue_date, dob)

        # Then the card should last exactly 10 years
        self.assertEqual(date(2009, 12, 31), expiration_date)

    def test_generate_expiration_date_person_over_60_at_issue(self):
        # Given
        issue_date = date(2000, 12, 31)
        dob = date(1940, 1, 1)

        # When
        expiration_date = self.provisional_licence_generator.generate_expiration_date(issue_date, dob)

        # Then the card should last up until the person's 70th birthday
        self.assertEqual(date(2010, 1, 1), expiration_date)

    def test_generate_expiration_date_person_over_70_at_issue(self):
        # Given
        issue_date = date(2010, 12, 31)
        dob = date(1940, 12, 31)

        # When
        expiration_date = self.provisional_licence_generator.generate_expiration_date(issue_date, dob)

        # Then the card should last only 3 years
        self.assertEqual(date(2013, 12, 31), expiration_date)

    def test_generate_issue_date_raises_when_person_under_15y_9m(self):
        """Test that an error is raised when the person is to young to hold a full licence """
        # Given
        dob = date(2000, 1, 2)
        today = date(2015, 9, 1)

        # When / Then
        with self.assertRaises(Exception):
            self.provisional_licence_generator.generate_issue_date(dob, today)

    def test_generate_issue_date_no_throw_when_person_15y_9m_or_older(self):
        """Test that a date is returned"""
        # Given
        dob = date(2000, 1, 2)
        today = date(2015, 9, 2)

        # When
        self.provisional_licence_generator.generate_issue_date(dob, today)

        # Then nothing is thrown so no assertion needed
