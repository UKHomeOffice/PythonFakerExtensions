import random
from faker import Faker
from faker.providers import BaseProvider
from faker_extensions.data import crime_types as crime

fake = Faker()

class ModusOperandiProvider(BaseProvider):

    def __init__(self, generator):
        super().__init__(generator)
        self.crime_types = list(crime.types_to_keywords.keys())

    def _category(self):
        return random.choice(self.crime_types)

    def _details(self):
        return fake.text()

    def _keywords(self, category):
        if len(crime.types_to_keywords[category]) > 0:
            return [random.choice(crime.types_to_keywords[category])]
        else:
            return [fake.word() for _ in range(random.randint(1, 10))]

    def modus_operandi(self):

        category = self._category()

        return {
            "category": category,
            "details":  self._details(),
            "keywords": self._keywords(category)
        }

def main():

    fake = Faker(['en_UK'])
    fake.add_provider(ModusOperandiProvider(fake))

    mo = fake.modus_operandi()
    print(mo)

if __name__ == '__main__':
    main()
