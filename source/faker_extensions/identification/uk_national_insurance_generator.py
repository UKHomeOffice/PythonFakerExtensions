from datetime import date
import random

from dateutil.relativedelta import relativedelta

from faker_extensions.abstract_providers import IdentityFormGenerator


class UkNationalInsuranceNumberGenerator(IdentityFormGenerator):
    """ Defines how issue and expiration dates are generated for a national insurance number """

    regex = "^([ABCEGHJKLMNOPRSTWZYZ][ABCEGHJKLMNPRSTWZYZ][0-9]{6}[ABCD])$"

    def generate_expiration_date(self, issue_date, dob):
        return None

    def generate_issue_date(self, dob, today):
        return dob + relativedelta(years=16)
