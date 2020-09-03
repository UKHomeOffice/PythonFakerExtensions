from faker import Faker

from faker_extensions.abstract_providers import CategoryWeightedProvider
from faker_extensions.data.military_ranks import military_rank_distributions, MilitaryService


class MilitaryRankProvider(CategoryWeightedProvider):
    def __init__(self, generator):
        super().__init__(military_rank_distributions, generator)

    def military_rank(self, rank):
        return self.get_choice(rank)


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(MilitaryRankProvider(fake))

    rank = fake.military_rank(MilitaryService.ROYAL_NAVY)
    print(MilitaryService.ROYAL_NAVY, rank)

    rank = fake.military_rank(MilitaryService.ROYAL_MARINES)
    print(MilitaryService.ROYAL_MARINES, rank)

    rank = fake.military_rank(MilitaryService.BRITISH_ARMY)
    print(MilitaryService.BRITISH_ARMY, rank)

    rank = fake.military_rank(MilitaryService.ROYAL_AIR_FORCE)
    print(MilitaryService.ROYAL_AIR_FORCE, rank)


if __name__ == '__main__':
    main()
