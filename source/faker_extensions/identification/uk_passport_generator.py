from datetime import date
import random

from dateutil.relativedelta import relativedelta

from faker_extensions.abstract_providers import IdentityFormGenerator


class UkPassportGenerator(IdentityFormGenerator):
    """ Defines how issue and expiration dates are generated for a passport """

    regex = "^[0-9]{10}GBR[0-9]{7}[U,M,F]{1}[0-9]{9}$"

    def generate_expiration_date(self, issue_date, dob):
        return issue_date + relativedelta(years=+10)

    def generate_issue_date(self, dob, today):
        return date.fromordinal(
            random.randint(dob.toordinal(), today.toordinal()))
