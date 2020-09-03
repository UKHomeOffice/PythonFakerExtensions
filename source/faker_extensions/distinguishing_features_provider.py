from enum import Enum
from random import randint

from faker import Faker
from faker_extensions.abstract_providers import CategoryWeightedProvider
from faker_extensions.common_categories import Gender, BaseEnum

""" List of distinguishing facial/body features in the UK """
''' Congenital: birth conditions like birthmarks, cleft lips/palates '''
''' Accidental: including burns and facial scars '''
''' cancer-related: from surgery for skin cancer '''
''' facial paralysis:  including from stroke '''
''' skin conditions like psoriasis, vitiligo and acne '''


class Features(BaseEnum):
    CLEIPS_LIPS_PALATES = 1
    BIRTH_MARKS = 2
    BURNS = 3
    SCARRING_FRACTURES = 4
    SKIN_CANCER = 5
    HEAD_NECK_CANCER = 6
    LOSS_OF_EYE_OR_SQUINT = 7
    BELLS_PALSY = 8
    STROKE = 9
    FACIAL_PSORIASIS = 10
    ACNE_ECZEMA = 11
    VITILIGO = 12


class BodyArea(BaseEnum):
    FACE = 1
    NECK = 2
    HEAD = 3
    RIBS = 4
    CHEST = 5
    BACKBONE = 6
    ABDOMEN = 7
    LOWER_BACK = 8
    SHOULDER = 9
    SHOULDER_BLADE = 10
    FOREARM = 11
    UPPER_ARM = 12
    WRIST = 13
    ELBOW = 14
    HAND = 15
    LOWER_LEG = 16
    THIGH = 17
    FOOT = 18
    KNEE = 19
    ANKLE = 20
    OTHER = 21


class FeaturesProvider(CategoryWeightedProvider):
    """ Distinguishing features distribution in the uk """
    features_distributions = {
        Gender.FEMALE: {
            Features.CLEIPS_LIPS_PALATES: 0.000677303,
            Features.BIRTH_MARKS: 0.002408188,
            Features.BURNS: 0.00090307,
            Features.SCARRING_FRACTURES: 0.005418423,
            Features.SKIN_CANCER: 0.001128838,
            Features.HEAD_NECK_CANCER: 0.000240819,
            Features.LOSS_OF_EYE_OR_SQUINT: 0.000376279,
            Features.BELLS_PALSY: 0.000602047,
            Features.STROKE: 0.00090307,
            Features.ACNE_ECZEMA: 0.001881397,
            Features.FACIAL_PSORIASIS: 0.003950933,
            Features.VITILIGO: 0.001128838
        },
        Gender.MALE: {
            Features.CLEIPS_LIPS_PALATES: 0.000677303,
            Features.BIRTH_MARKS: 0.002408188,
            Features.BURNS: 0.00090307,
            Features.SCARRING_FRACTURES: 0.005418423,
            Features.SKIN_CANCER: 0.001128838,
            Features.HEAD_NECK_CANCER: 0.000240819,
            Features.LOSS_OF_EYE_OR_SQUINT: 0.000376279,
            Features.BELLS_PALSY: 0.000602047,
            Features.STROKE: 0.00090307,
            Features.ACNE_ECZEMA: 0.001881397,
            Features.FACIAL_PSORIASIS: 0.003950933,
            Features.VITILIGO: 0.001128838
        }
    }

    def body_area_selector(self, distinguishing_feature):
        """ Returns distinguishing feature with body area """
        body_area_selector = {
            Features.HEAD_NECK_CANCER: BodyArea.NECK,
            Features.CLEIPS_LIPS_PALATES: BodyArea.FACE,
            Features.LOSS_OF_EYE_OR_SQUINT: BodyArea.FACE,
            Features.BELLS_PALSY: BodyArea.FACE,
            Features.STROKE: BodyArea.FACE,
            Features.ACNE_ECZEMA: BodyArea.FACE,
            Features.FACIAL_PSORIASIS: BodyArea.FACE,
            Features.VITILIGO: BodyArea.FACE
        }
        random_body_area = BodyArea(randint(1, len(BodyArea.__members__)))
        return body_area_selector.get(distinguishing_feature, random_body_area)

    def __init__(self, generator):
        super().__init__(self.features_distributions, generator)

    def features(self, category):
        """ Returns distinguishing feature with body area """
        distinguishing_feature = self.get_choice(category)
        return {distinguishing_feature, self.body_area_selector(distinguishing_feature)}


def main():
    fake = Faker(['en_UK'])
    fake.add_provider(FeaturesProvider(fake))
    features = fake.features(Gender.MALE)
    print(Gender.MALE)
    print(features)
    features = fake.features(Gender.FEMALE)
    print(Gender.FEMALE)
    print(features)


if __name__ == '__main__':
    main()
