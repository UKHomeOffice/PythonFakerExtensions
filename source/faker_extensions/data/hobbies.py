#  https://theharrispoll.com/wp-content/uploads/2017/12/Harris-Interactive-Poll-Research-Work-Leisure-2007-11.pdf
from enum import Enum

import stringcase


class Hobbies(Enum):
    READING = 1
    TV_WATCHING = 2
    SPENDING_TIME_WITH_FAMILY = 3
    COMPUTER_ACTIVITIES = 4
    GOING_TO_MOVIES = 5
    FISHING = 6
    GARDENING = 7
    WALKING = 8
    PLAYING_TEAM_SPORTS = 9
    EXERCISE = 10
    GOLF = 11
    CHURCH_ACTIVITIES = 12
    LISTENING_TO_MUSIC = 13
    WATCHING_SPORTING_EVENTS = 14
    SHOPPING = 15
    SOCIALISING = 16
    TRAVELING = 17
    PLAYING_MUSIC = 18
    ENTERTAINING = 19
    RENTING_MOVIES = 20
    EATING_OUT = 21
    HUNTING = 22
    CRAFTS = 23
    SWIMMING = 24
    CAMPING = 25
    BICYCLING = 26
    OUTDOOR_ACTIVITIES = 27
    SEWING_OR_CROCHETING = 28
    RELAXING = 29
    PLAYING_CARDS = 30
    HIKING = 31
    HOUSEWORK = 32
    COOKING = 33
    WORKING_ON_CARS = 34
    BOATING = 35
    ANIMALS = 36
    PAINTING = 37
    DANCING = 38
    HORSEBACK_RIDING = 39
    SLEEPING = 40
    RUNNING = 41
    WRITING = 42
    BOWLING = 43
    MOTORCYCLING = 44
    WOODWORKING = 45
    SKIING = 46
    TENNIS = 47

    def name_value(self):
        return stringcase.sentencecase(self.name.lower())


hobby_distributions = {
    Hobbies.READING: 0.29,
    Hobbies.TV_WATCHING: 0.18,
    Hobbies.SPENDING_TIME_WITH_FAMILY: 0.14,
    Hobbies.COMPUTER_ACTIVITIES: 0.09,
    Hobbies.GOING_TO_MOVIES: 0.07,
    Hobbies.FISHING: 0.07,
    Hobbies.GARDENING: 0.06,
    Hobbies.WALKING: 0.06,
    Hobbies.PLAYING_TEAM_SPORTS: 0.06,
    Hobbies.EXERCISE: 0.05,
    Hobbies.GOLF: 0.05,
    Hobbies.CHURCH_ACTIVITIES: 0.05,
    Hobbies.LISTENING_TO_MUSIC: 0.04,
    Hobbies.WATCHING_SPORTING_EVENTS: 0.04,
    Hobbies.SHOPPING: 0.04,
    Hobbies.SOCIALISING: 0.04,
    Hobbies.TRAVELING: 0.04,
    Hobbies.PLAYING_MUSIC: 0.03,
    Hobbies.ENTERTAINING: 0.03,
    Hobbies.RENTING_MOVIES: 0.03,
    Hobbies.EATING_OUT: 0.03,
    Hobbies.HUNTING: 0.03,
    Hobbies.CRAFTS: 0.03,
    Hobbies.SWIMMING: 0.03,
    Hobbies.CAMPING: 0.03,
    Hobbies.BICYCLING: 0.03,
    Hobbies.OUTDOOR_ACTIVITIES: 0.03,
    Hobbies.SEWING_OR_CROCHETING: 0.02,
    Hobbies.RELAXING: 0.02,
    Hobbies.PLAYING_CARDS: 0.02,
    Hobbies.HIKING: 0.02,
    Hobbies.HOUSEWORK: 0.02,
    Hobbies.COOKING: 0.02,
    Hobbies.WORKING_ON_CARS: 0.02,
    Hobbies.BOATING: 0.02,
    Hobbies.ANIMALS: 0.02,
    Hobbies.PAINTING: 0.02,
    Hobbies.DANCING: 0.02,
    Hobbies.HORSEBACK_RIDING: 0.02,
    Hobbies.SLEEPING: 0.01,
    Hobbies.RUNNING: 0.01,
    Hobbies.WRITING: 0.01,
    Hobbies.BOWLING: 0.01,
    Hobbies.MOTORCYCLING: 0.01,
    Hobbies.WOODWORKING: 0.01,
    Hobbies.SKIING: 0.01,
    Hobbies.TENNIS: 0.01
}
