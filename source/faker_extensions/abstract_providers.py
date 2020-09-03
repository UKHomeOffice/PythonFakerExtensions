import abc
import random
from random import randint

from faker.providers import BaseProvider


# Question: Should we use inheritance here or association.  Association feels more useful in terms of
# creating new providers.  But the data input would be more complex


class WeightedProvider(BaseProvider):
    """A provider that uses a dictionary of keys and weightings for those keys"""

    def __init__(self, di, generator):
        if type(self) == WeightedProvider:
            raise Exception("<WeightedProvider> must be subclassed.")
        super().__init__(generator)
        self._population = list(di.keys())
        self._weights = list(di.values())

    def get_choice(self):
        return random.choices(self._population, weights=self._weights)[0]


class BoundedWeightedProvider(WeightedProvider):
    """A provider that uses a dictionary of bounds and weightings for those keys"""

    def __init__(self, di, generator):
        if type(self) == BoundedWeightedProvider:
            raise Exception("<BoundedWeightedProvider> must be subclassed.")
        super().__init__(di, generator)

    """ Override the get choice to give back a value inside the tuple"""

    def get_choice(self):
        tpl = super().get_choice()
        return randint(tpl[0], tpl[1])


class CategoryWeightedProvider(BaseProvider):
    """A provider that uses a dictionary of keys and weightings for those keys"""

    def __init__(self, di, generator):
        if type(self) == CategoryWeightedProvider:
            raise Exception("<CategoryWeightedProvider> must be subclassed.")
        super().__init__(generator)
        # We have a dictionary of dictionaries
        # We need to map that into a dictionary of categories
        self.data = {key: (list(value.keys()), list(value.values())) for key, value in di.items()}

    def get_choice(self, category):
        return random.choices(self.data[category][0], weights=self.data[category][1])[0]


class CategoryBoundWeightedProvider(CategoryWeightedProvider):
    """A provider that uses a dictionary of dictionary of keys and weightings for those keys"""

    def __init__(self, di, generator):
        if type(self) == CategoryBoundWeightedProvider:
            raise Exception("<CategoryBoundWeightedProvider> must be subclassed.")
        super().__init__(di, generator)

    def get_choice(self, category):
        tpl = random.choices(self.data[category][0], weights=self.data[category][1])[0]
        return randint(tpl[0], tpl[1])


class NormalProvider(BaseProvider):
    """A provider that produces results based on a normal or gaussian distribution"""

    def __init__(self, mean, std, generator):
        super().__init__(generator)
        if type(self) == NormalProvider:
            raise Exception("<NormalProvider> must be subclassed.")
        self._mean = mean
        self._std = std

    def get_choice(self):
        return random.gauss(self._mean, self._std)


class CategoricalNormalProvider(BaseProvider):
    """A provider that produces results based on a normal or gaussian distribution"""

    def __init__(self, di, generator):
        super().__init__(generator)
        if type(self) == CategoricalNormalProvider:
            raise Exception("<CategoricalNormalProvider> must be subclassed.")
        self._di = di

    def get_choice(self, category):
        return random.gauss(self._di[category][0], self._di[category][1])


class DictionaryProvider(BaseProvider):
    """Returns a dictionary from a list of dictionaries"""

    def __init__(self, li, generator):
        if type(self) == DictionaryProvider:
            raise Exception("<DictionaryProvider> must be subclassed.")
        super().__init__(generator)
        self._li = li

    def get_choice(self):
        return random.choice(self._li)


class IdentityFormGenerator(abc.ABC):
    """ Defines the methods a IdentityFormDetailGenerator must implement """

    @property
    @abc.abstractmethod
    def regex(self):
        """ the regex representing a valid identity document """
        pass

    @abc.abstractmethod
    def generate_issue_date(self, dob, today):
        """ generates the date the identity was issued """

    @abc.abstractmethod
    def generate_expiration_date(self, issue_date, dob):
        """ generates the date the identity expires """
