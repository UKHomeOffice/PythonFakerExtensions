from datetime import date
import random

from dateutil.relativedelta import relativedelta

from faker_extensions.abstract_providers import IdentityFormGenerator


class UkProvisionalDrivingLicenceGenerator(IdentityFormGenerator):
    """ Defines how issue and expiration dates are generated for a full uk driving licence """

    regex = "^([A-Z]{2}[9]{3}|[A-Z]{3}[9]{2}|[A-Z]{4}[9]{1}|" \
            "[A-Z]{5})[0-9]{6}([A-Z]{1}[9]{1}|[A-Z]{2})[A-Z0,9]{3}$"

    def generate_expiration_date(self, issue_date, dob):
        """ Licence cards will need replaced every 10 years up until 70, when a new licence will
        need issued and then will need replaced every 3 years.
        todo: verify this logic and add unit tests """

        age_at_issue = relativedelta(issue_date, dob).years

        if age_at_issue >= 70:  # the person is over 70
            return issue_date + relativedelta(years=+3)
        elif age_at_issue >= 60:  # the person will turn 70 within the next 10 years
            return dob + relativedelta(years=+70)  # return 70th birthday
        # the person is under 70 and will not turn 70 in the next 10 years
        else:
            return issue_date + relativedelta(years=+10)

    def generate_issue_date(self, dob, today):
        age = relativedelta(date.today(), dob).years

        date_person_is_15y_9m = dob + relativedelta(years=+15, month=+9)

        if today < date_person_is_15y_9m:
            raise Exception(
                "Person must be 15 years and 9 months or over to hold provisional uk driving "
                "licence")

        return date.fromordinal(
            random.randint(date_person_is_15y_9m.toordinal(),
                           today.toordinal()))
