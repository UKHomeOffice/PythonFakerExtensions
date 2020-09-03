from enum import Enum

import stringcase


class DeviceManufacturer(Enum):
    APPLE = 1
    SAMSUNG = 2
    HUAWEI = 3
    SONY = 4
    MOTOROLA = 5
    GOOGLE = 6
    ONEPLUS = 7
    # UNKNOWN = 8
    XIAOMI = 9
    NOKIA = 10
    LENOVO = 11
    LG = 12
    HTC = 13
    ALCATEL = 14
    VODAFONE = 15

    def name_value(self):
        return stringcase.sentencecase(self.name.lower())


# https://gs.statcounter.com/vendor-market-share/mobile/united-kingdom/2019
# information taken from source was then averaged over the year

device_manufacturer_distributions = {
    DeviceManufacturer.APPLE: 0.492,
    DeviceManufacturer.SAMSUNG: 0.295,
    DeviceManufacturer.HUAWEI: 0.0819,
    DeviceManufacturer.SONY: 0.0218,
    DeviceManufacturer.MOTOROLA: 0.0189,
    DeviceManufacturer.GOOGLE: 0.0125,
    DeviceManufacturer.ONEPLUS: 0.0123,
    #  DeviceManufacturer.UNKNOWN: 0.0123,
    DeviceManufacturer.XIAOMI: 0.0104,
    DeviceManufacturer.NOKIA: 0.0085,
    DeviceManufacturer.LENOVO: 0.0084,
    DeviceManufacturer.LG: 0.0075,
    DeviceManufacturer.HTC: 0.0048,
    DeviceManufacturer.ALCATEL: 0.0024,
    DeviceManufacturer.VODAFONE: 0.0021,
}


# Jan 2017-May 2020 Apple Phones
class Apple(Enum):
    IPHONE_SE_2ND_GEN = "iPhone SE Second Generation"
    IPHONE_11_PRO_MAX = "iPhone 11 Pro Max"
    IPHONE_11_PRO = "iPhone 11 Pro"
    IPHONE_11 = "iPhone 11"
    IPHONE_XR = "iPhone XR"
    IPHONE_XS_MAX = "iPhone XS Max"
    IPHONE_XS = "iPhone XS"
    IPHONE_X = "iPhone X"
    IPHONE_8_Plus = "iPhone 8 Plus"
    IPHONE_8 = "iPhone 8"


# 1 Jan 2017-May 2020 Samsung Phones
class Samsung(Enum):
    # Note
    SAMSUNG_GALAXY_NOTE10_LITE = "Samsung Galaxy Note 10 Lite"
    SAMSUNG_GALAXY_NOTE10_PLUS_5G = "Samsung Galaxy Note10+ 5G"
    SAMSUNG_GALAXY_NOTE9 = "Samsung Galaxy Note9"
    SAMSUNG_GALAXY_NOTE8 = "Samsung Galaxy Note8"
    SAMSUNG_GALAXY_NOTE_FAN_EDITION = "Samsung Galaxy Note Fan Edition"

    # S Series
    SAMSUNG_GALAXY_S20_ULTRA = "Samsung Galaxy S20 Ultra"
    SAMSUNG_GALAXY_S20_PLUS = "Samsung Galaxy S20+"
    SAMSUNG_GALAXY_S20 = "Samsung Galaxy S20"
    SAMSUNG_GALAXY_S10_LITE = "Samsung Galaxy S10 Lite"
    SAMSUNG_GALAXY_S10_5G = "Samsung Galaxy S10 5G"
    SAMSUNG_GALAXY_S10_PLUS = "Samsung Galaxy S10+"
    SAMSUNG_GALAXY_S10 = "Samsung Galaxy S10"
    SAMSUNG_GALAXY_S10E = "Samsung Galaxy S10e"
    SAMSUNG_GALAXY_S9_PLUS = "Samsung Galaxy S9+"
    SAMSUNG_GALAXY_S9 = "Samsung Galaxy S9"
    SAMSUNG_GALAXY_S8_ACTIVE = "Samsung Galaxy S8 Active"
    SAMSUNG_GALAXY_S8_PLUS = "Samsung Galaxy S8+"
    SAMSUNG_GALAXY_S8 = "Samsung Galaxy S8"

    # A Series
    SAMSUNG_GALAXY_A51 = "Samsung Galaxy A51"
    SAMSUNG_GALAXY_A71 = "Samsung Galaxy A71"
    SAMSUNG_GALAXY_A01 = "Samsung Galaxy A01"
    SAMSUNG_GALAXY_A11 = "Samsung Galaxy A11"
    SAMSUNG_GALAXY_A41 = "Samsung Galaxy A41"
    SAMSUNG_GALAXY_A31 = "Samsung Galaxy A31"
    SAMSUNG_GALAXY_A21 = "Samsung Galaxy A21"
    SAMSUNG_GALAXY_A51_5G = "Samsung Galaxy A51 5G"
    SAMSUNG_GALAXY_A71_5G = "Samsung Galaxy A71 5G"
    SAMSUNG_GALAXY_A30 = "Samsung Galaxy A30"
    SAMSUNG_GALAXY_A50 = "Samsung Galaxy A50"
    SAMSUNG_GALAXY_A10 = "Samsung Galaxy A10"
    SAMSUNG_GALAXY_A20 = "Samsung Galaxy A20"
    SAMSUNG_GALAXY_A40 = "Samsung Galaxy A40"
    SAMSUNG_GALAXY_A70 = "Samsung Galaxy A70"
    SAMSUNG_GALAXY_A20E = "Samsung Galaxy A20e"
    SAMSUNG_GALAXY_A80 = "Samsung Galaxy A80"
    SAMSUNG_GALAXY_A40S = "Samsung Galaxy A40s"
    SAMSUNG_GALAXY_A60 = "Samsung Galaxy A60"
    SAMSUNG_GALAXY_A2_CORE = "Samsung Galaxy A2 Core"
    SAMSUNG_GALAXY_A10S = "Samsung Galaxy A10s"
    SAMSUNG_GALAXY_A20S = "Samsung Galaxy A20s"
    SAMSUNG_GALAXY_A10E = "Samsung Galaxy A10e"
    SAMSUNG_GALAXY_A30S = "Samsung Galaxy A30s"
    SAMSUNG_GALAXY_A50S = "Samsung Galaxy A50s"
    SAMSUNG_GALAXY_A90_5G = "Samsung Galaxy A90 5G"
    SAMSUNG_GALAXY_A70S = "Samsung Galaxy A70s"
    SAMSUNG_GALAXY_A8 = "Samsung Galaxy A8"
    SAMSUNG_GALAXY_A8_PLUS = "Samsung Galaxy A8+"
    SAMSUNG_GALAXY_A6 = "Samsung Galaxy A6"
    SAMSUNG_GALAXY_A6_PLUS = "Samsung Galaxy A6+"
    SAMSUNG_GALAXY_A8_STAR = "Samsung Galaxy A8 Star"
    SAMSUNG_GALAXY_A7_2018 = "Samsung Galaxy A7 (2018)"
    SAMSUNG_GALAXY_A9_2018 = "Samsung Galaxy A9 (2018)"
    SAMSUNG_GALAXY_A6S = "Samsung Galaxy A6s"
    SAMSUNG_GALAXY_A8S = "Samsung Galaxy A8s"
    SAMSUNG_GALAXY_A3_2017 = "Samsung Galaxy A3 (2017)"
    SAMSUNG_GALAXY_A5_2017 = "Samsung Galaxy A5 (2017)"
    SAMSUNG_GALAXY_A7_2017 = "Samsung Galaxy A7 (2017)"

    # J Series
    SAMSUNG_GALAXY_J2_PRO = "Samsung Galaxy J2 Pro"
    SAMSUNG_GALAXY_J7_PRIME_2 = "Samsung Galaxy J7 Prime 2"
    SAMSUNG_GALAXY_J7_DUO = "Samsung Galaxy J7 Duo"
    SAMSUNG_GALAXY_J4 = "Samsung Galaxy J4"
    SAMSUNG_GALAXY_J6 = "Samsung Galaxy J6"
    SAMSUNG_GALAXY_J3_2018 = "Samsung Galaxy J3 (2018)"
    SAMSUNG_GALAXY_J8 = "Samsung Galaxy J8"
    SAMSUNG_GALAXY_J7_2018 = "Samsung Galaxy J7 (2018)"
    SAMSUNG_GALAXY_J2_CORE = "Samsung Galaxy J2 Core"
    SAMSUNG_GALAXY_J4_PLUS = "Samsung Galaxy J4+"
    SAMSUNG_GALAXY_J6_PLUS = "Samsung Galaxy J6+"
    SAMSUNG_GALAXY_J3_EMERGE = "Samsung Galaxy J3 Emerge"
    SAMSUNG_GALAXY_J7_V = "Samsung Galaxy J7 V"
    SAMSUNG_GALAXY_J3_PRIME = "Samsung Galaxy J3 Prime"
    SAMSUNG_GALAXY_J3_2017 = "Samsung Galaxy J3 (2017)"
    SAMSUNG_GALAXY_J5_2017 = "Samsung Galaxy J5 (2017)"
    SAMSUNG_GALAXY_J7_2017 = "Samsung Galaxy J7 (2017)"
    SAMSUNG_GALAXY_J7_PRO = "Samsung Galaxy J7 Pro"
    SAMSUNG_GALAXY_J7_MAX = "Samsung Galaxy J7 Max"
    SAMSUNG_GALAXY_J7_NXT = "Samsung Galaxy J7 Nxt"
    SAMSUNG_GALAXY_J3_LUNA_PRO = "Samsung Galaxy J3 Luna Pro"

    # M Series
    SAMSUNG_GALAXY_M31 = "Samsung_Galaxy_M31"
    SAMSUNG_GALAXY_M21 = "Samsung_Galaxy_M21"
    SAMSUNG_GALAXY_M11 = "Samsung_Galaxy_M11"
    SAMSUNG_GALAXY_M10 = "Samsung_Galaxy_M10"
    SAMSUNG_GALAXY_M20 = "Samsung_Galaxy_M20"
    SAMSUNG_GALAXY_M30 = "Samsung_Galaxy_M30"
    SAMSUNG_GALAXY_M40 = "Samsung_Galaxy_M40"
    SAMSUNG_GALAXY_M10S = "Samsung_Galaxy_M10s"
    SAMSUNG_GALAXY_M30S = "Samsung_Galaxy_M30s"

    # On Series
    SAMSUNG_GALAXY_ON_MAX = "Samsung Galaxy On Max"
    SAMSUNG_GALAXY_ON7_PRIME = "Samsung Galaxy On7 Prime"
    SAMSUNG_GALAXY_ON6 = "Samsung Galaxy On6"
    SAMSUNG_GALAXY_ON8 = "Samsung Galaxy On8"

    # C Series
    Samsung_Galaxy_C5_Pro = "Samsung Galaxy C5 Pro"
    Samsung_Galaxy_C7_2017 = "Samsung Galaxy C7 (2017)"
    Samsung_Galaxy_C7_Pro = "Samsung Galaxy C7 Pro"
    Samsung_Galaxy_C8 = "Samsung Galaxy C8"

    # Other
    Samsung_Galaxy_Folder_2 = "Samsung Galaxy Folder 2"
    Samsung_Galaxy_Feel = "Samsung Galaxy Feel"
    Samsung_Galaxy_Feel2 = "Samsung Galaxy Feel2"
    Samsung_Galaxy_Fold = "Samsung Galaxy Fold"
    Samsung_Galaxy_Z_Flip = "Samsung Galaxy Z Flip"


# Jan 2017-May 2020 Huawei Phones
class Huawei(Enum):
    # Mate Series
    HUAWEI_MATE_10 = "Huawei Mate 10"
    HUAWEI_MATE_10_PRO = "Huawei Mate 10 Pro"
    HUAWEI_MATE_10_LITE = "Huawei Mate 10 Lite"
    HUAWEI_PORSCHE_DESIGN_MATE_10 = "Huawei Porsche Design Mate 10"
    HUAWEI_PORSCHE_DESIGN_MATE_RS = "Huawei Porsche Design Mate RS"
    HUAWEI_MATE_20 = "Huawei Mate 20 (20"
    HUAWEI_MATE_20_PRO = "Huawei Mate 20 Pro"
    HUAWEI_MATE_20_LITE = "Huawei Mate 20 Lite"
    HUAWEI_MATE_20_X = "Huawei Mate 20 X"
    HUAWEI_MATE_20_PORSCHE_RS = "Huawei Mate 20 Porsche RS"
    HUAWEI_MATE_X = "Huawei Mate X"
    HUAWEI_MATE_30 = "Huawei Mate 30"
    HUAWEI_MATE_30_PRO = "Huawei Mate 30 Pro"
    HUAWEI_MATE_30_5G = "Huawei Mate 30 (5G)"
    HUAWEI_MATE_30_PRO_5G = "Huawei Mate 30 Pro (5G)"
    HUAWEI_MATE_30_RS = "Huawei Mate 30 RS"
    HUAWEI_MATE_XS = "Huawei Mate Xs"

    # P series
    HUAWEI_P8_LITE_HONOR_8_LITE = "Huawei P8 Lite (Honor 8 Lite)"
    HUAWEI_P9_LITE_MINI = "Huawei P9 Lite Mini"
    HUAWEI_P10 = "Huawei P10"
    HUAWEI_P10_PLUS = "Huawei P10 Plus"
    HUAWEI_P10_LITE_NOVA_LITE = "Huawei P10 Lite (Nova Lite)"
    HUAWEI_P_SMART = "Huawei P Smart "
    HUAWEI_P_SMART_PRO = "Huawei P Smart Pro "
    HUAWEI_P20 = "Huawei P20 "
    HUAWEI_P20_PRO = "Huawei P20 Pro "
    HUAWEI_P20_LITE = "Huawei P20 Lite"
    HUAWEI_P_SMART_PLUS = "Huawei P Smart +"
    HUAWEI_P_SMART_Z = "Huawei P Smart Z"
    HUAWEI_P30 = "Huawei P30"
    HUAWEI_P30_PRO = "Huawei P30 Pro"
    HUAWEI_P30_LITE = "Huawei P30 Lite"
    HUAWEI_P40 = "Huawei P40"
    HUAWEI_P40_LITE = "Huawei P40 Lite"
    HUAWEI_P40_LITE_E = "Huawei P40 Lite E"
    HUAWEI_P40_PRO = "Huawei P40 Pro"
    HUAWEI_P40_PRO_PLUS = "Huawei P40 Pro+"

    # Nova Series
    NOVA_2_LITE = "Nova 2 Lite"
    NOVA_2 = "Nova 2"
    NOVA_2_PLUS = "Nova 2 Plus"
    NOVA_2I = "Nova 2i"
    NOVA_2S = "Nova 2s"
    NOVA_3E = "Nova 3e"
    NOVA_3I = "Nova 3i"
    NOVA_4E = "Nova 4e"
    NOVA_4 = "Nova 4"
    NOVA_5I_PRO = "Nova 5i Pro"
    NOVA_5T = "Nova 5T"
    NOVA_5 = "Nova 5"
    NOVA_6_SE = "Nova 6 SE"
    NOVA_6_AND_6_5G = "Nova 6 & 6 5G"
    NOVA_7_SE = "Nova 7 SE"
    NOVA_7 = "Nova 7"
    NOVA_7_PRO = "Nova 7 Pro"

    # GR Series
    HUAWEI_GR5 = "Huawei Gr5"
    HUAWEI_GR3 = "Huawei Gr3"

    # Y Series
    HUAWEI_Y7 = "Huawei Y7"
    HUAWEI_Y7_PRIME = "Huawei Y7 prime"
    HUAWEI_Y7P = "Huawei Y7p"
    HUAWEI_Y9 = "Huawei Y9"
    HUAWEI_Y9_PRIME = "Huawei Y9 Prime"
    HUAWEI_Y_MAX = "Huawei Y max"
    HUAWEI_Y9S = "Huawei Y9s"
    HUAWEI_Y3 = "Huawei Y3"
    HUAWEI_Y5 = "Huawei Y5"
    HUAWEI_Y5_LITE = "Huawei Y5 Lite"
    HUAWEI_Y5_PRIME = "Huawei Y5 Prime"
    HUAWEI_Y6 = "Huawei Y6"
    HUAWEI_Y7_PRO = "Huawei Y7 Pro"
    HUAWEI_Y8 = "Huawei Y8"

    # Honor
    HONOR_8_LITE = "Honor 8 Lite "
    HONOR_V8 = "Honor V8 "
    HONOR_8_PRO = "Honor 8 Pro"
    HONOR_9 = "Honor 9"
    HONOR_9_LITE = "Honor 9 Lite"
    HONOR_9I = "Honor 9i"
    HONOR_VIEW_10 = "Honor View 10"
    HONOR_VIEW_20 = "Honor View 20"
    HONOR_10 = "Honor 10"
    HONOR_10_GT = "Honor 10 GT"
    HONOR_10_LITE = "Honor 10 Lite"
    HONOR_PLAY = "Honor Play"
    HONOR_NOTE_10 = "Honor Note 10"
    HONOR_8X = "Honor 8X"
    HONOR_8X_MAX = "Honor 8X Max"
    HONOR_8C = "Honor 8C"
    HONOR_MAGIC = "Honor Magic"
    HONOR_MAGIC_2 = "Honor Magic 2"
    HONOR_8A = "Honor 8A"


# Jan 2017-May 2020 Sony Phones
class Sony(Enum):
    XPERIA_XZS = "Xperia XZs"
    XPERIA_XZ_PREMIUM = "Xperia XZ Premium"
    XPERIA_XA1 = "Xperia XA1"
    XPERIA_XA1_ULTRA = "Xperia XA1 Ultra"
    XPERIA_L1 = "Xperia L1"
    XPERIA_XZ1 = "Xperia XZ1"
    XPERIA_XZ1_COMPACT = "Xperia XZ1 Compact"
    XPERIA_XA1_PLUS = "Xperia XA1 Plus"
    XPERIA_R1 = "Xperia R1"
    XPERIA_R1_PLUS = "Xperia R1 Plus"
    XPERIA_L2 = "Xperia L2"
    XPERIA_XA2 = "Xperia XA2"
    XPERIA_XA2_ULTRA = "Xperia XA2 Ultra"
    XPERIA_XZ2 = "Xperia XZ2"
    XPERIA_XZ2_COMPACT = "Xperia XZ2 Compact"
    XPERIA_XZ2_PREMIUM = "Xperia XZ2 Premium"
    XPERIA_XA2_PLUS = "Xperia XA2 Plus"
    XPERIA_XZ3 = "Xperia XZ3"
    XPERIA_L3 = "Xperia L3"
    XPERIA_10 = "Xperia 10"
    XPERIA_10_PLU = "Xperia 10 Plu"
    XPERIA_1 = "Xperia 1"
    XPERIA_ACE = "Xperia Ace"
    XPERIA_5 = "Xperia 5"
    XPERIA_8 = "Xperia 8"
    XPERIA_L4 = "Xperia L4"
    XPERIA_1_II = "Xperia 1 II"
    XPERIA_10_II = "Xperia 10 II"
    XPERIA_PRO = "Xperia PRO"


# Jan 2017-May 2020 Motorola Phones
class Motorola(Enum):
    # C series
    MOTO_C = "Moto C"
    MOTO_C_PLUS = "Moto C Plus"

    # E series
    MOTO_E4 = "Moto E4"
    MOTO_E4_PLUS = "Moto E4 Plus"
    MOTO_E5 = "Moto E5"
    MOTO_E5_PLAY = "Moto E5 Play"
    MOTO_E5_PLUS = "Moto E5 Plus"
    MOTO_E6 = "Moto E6"
    MOTO_E6_PLAY = "Moto E6 Play"
    MOTO_E6_PLUS = "Moto E6 Plus"
    MOTO_E6S = "Moto E6s"

    # Edge
    MOTOROLA_EDGE = "Motorola Edge"
    MOTOROLA_EDGE_PLUS = "Motorola Edge+"

    # G Series
    MOTO_G5 = "Moto G5"
    MOTO_G5_PLUS = "Moto G5 Plus"
    MOTO_G5S = "Moto G5S"
    MOTO_G5S_PLUS = "Moto G5S Plus"
    MOTO_G6 = "Moto G6"
    MOTO_G6_PLAY = "Moto G6 Play"
    MOTO_G6_PLUS = "Moto G6 Plus"
    MOTO_G7 = "Moto G7"
    MOTO_G7_PLAY = "Moto G7 Play"
    MOTO_G7_POWER = "Moto G7 Power"
    MOTO_G7_PLUS = "Moto G7 Plus"
    MOTO_G8_PLAY = "Moto G8 Play"
    MOTO_G8_PLUS = "Moto G8 Plus"
    MOTO_G8 = "Moto G8"
    MOTO_G8_POWER = "Moto G8 Power"
    MOTO_G8_POWER_LITE = "Moto G8 Power Lite"
    MOTO_G_POWER = "Moto G Power"
    MOTO_G_STYLUS = "Moto G Stylus"

    # One series
    MOTOROLA_ONE = "Motorola One"
    MOTOROLA_ONE_POWER = "Motorola One Power"
    MOTOROLA_ONE_VISION = "Motorola One Vision"
    MOTOROLA_ONE_ACTION = "Motorola One Action"
    MOTOROLA_ONE_ZOOM = "Motorola One Zoom"
    MOTOROLA_ONE_MACRO = "Motorola One Macro"
    MOTOROLA_ONE_HYPER = "Motorola One Hyper"
    MOTOROLA_ONE_FUSION = "Motorola One Fusion"

    # X series
    MOTO_X4 = "Moto X4"

    # Z series
    MOTO_Z2_PLAY = "Moto Z2 Play"
    MOTO_Z2_FORCE_EDITION = "Moto Z2 Force Edition"
    MOTO_Z3 = "Moto Z3"
    MOTO_Z3_PLAY = "Moto Z3 Play"
    MOTO_Z4 = "Moto Z4"


# 1 Jan 2017-May 2020 Google Phones
class Google(Enum):
    PIXEL_2 = "Pixel 2"
    PIXEL_3 = "Pixel 3"
    PIXEL_4 = "Pixel 4"


# Jan 2017-May 2020 OnePlus Phones
class OnePlus(Enum):
    ONEPLUS_5 = "OnePlus 5"
    ONEPLUS_5T = "OnePlus 5T"
    ONEPLUS_6 = "OnePlus 6"
    ONEPLUS_6T = "OnePlus 6T"
    ONEPLUS_7 = "OnePlus 7"
    ONEPLUS_7_PRO = "OnePlus 7 Pro"
    ONEPLUS_7T = "OnePlus 7T"
    ONEPLUS_7T_PRO = "OnePlus 7T Pro"
    ONEPLUS_8 = "OnePlus 8"
    ONEPLUS_8_PRO = "OnePlus 8 Pro"


# Jan 2017-May 2020 Xiaomi Phones
class Xiaomi(Enum):
    Mi_Note_3 = "Mi Note 3"
    Mi_Note_10 = "Mi Note 10"
    Mi_Note_10_Pro = "Mi Note 10 Pro"
    Mi_Note_10_Lite = "Mi Note 10 Lite"
    Mi_MIX_2 = "Mi MIX 2"
    Mi_MIX_2S = "Mi MIX 2S"
    Mi_MIX_3 = "Mi MIX 3"
    Mi_MIX_3_5G = "Mi MIX 3 5G"


# Jan 2017-May 2020 Nokia Phones
class Nokia(Enum):
    NOKIA_105 = "Nokia 105"
    NOKIA_130 = "Nokia 130"
    NOKIA_110 = "Nokia 110"


# Jan 2017-May 2020 Lenovo Phones
class Lenovo(Enum):
    K7 = "K7"
    K10_PLUS = "K10 Plus"
    K10_NOTE = "K10 Note"
    A6_NOTE = "A6 Note"
    K8_NOTE = "K8 Note"
    Z6 = "Z6"
    Z6_PRO_5G = "Z6 Pro 5G"
    Z6_YOUTH = "Z6 Youth"
    Z6_PRO = "Z6 Pro"
    K6_ENJOY = "K6 Enjoy"
    S5_PRO_GT = "S5 Pro GT"
    K5_PRO = "K5 Pro"
    K9 = "K9"
    Z5 = "Z5"
    K5_NOTE = "K5 Note"
    A5 = "A5"
    K5 = "K5"
    K5_PLAY = "K5 play"
    S5 = "S5"
    K320T = "K320t"
    K8_PLUS = "K8 Plus"
    K8 = "K8"


# Jan 2017-May 2020 LG Phones
class LG(Enum):
    VELVET = "Velvet"
    FOLDER_2 = "Folder 2"
    V60_THINQ_5G = "V60 ThinQ 5G"
    Q51 = "Q51"
    W10_ALPHA = "W10 Alpha"
    K61 = "K61"
    K51S = "K51S"
    K41S = "K41S"
    V50S_THINQ_5G = "V50S ThinQ 5G"
    G8X_THINQ = "G8X ThinQ"
    Q70 = "Q70"
    K30 = "K30"
    K20 = "K20"
    K40S = "K40S"
    K50S = "K50S"
    W30_PRO = "W30 Pro"
    W30 = "W30"
    W10 = "W10"
    STYLO_5 = "Stylo 5"
    V50_THINQ_5G = "V50 ThinQ 5G"
    G8S_THINQ = "G8S ThinQ"
    G8_THINQ = "G8 ThinQ"
    Q60 = "Q60"
    K50 = "K50"
    K40 = "K40"
    Q9 = "Q9"
    V40_THINQ = "V40 ThinQ"
    TRIBUTE_EMPIRE = "Tribute Empire"
    CANDY = "Candy"
    G7_FIT = "G7 Fit"
    G7_ONE = "G7 One"
    Q8 = "Q8"
    K11_PLUS = "K11 Plus"
    Q_STYLO_4 = "Q Stylo 4"
    Q_STYLUS = "Q Stylus"
    V35_THINQ = "V35 ThinQ"
    Q7 = "Q7"
    Q7_THINQ = "Q7 ThinQ"
    V30S_THINQ = "V30S ThinQ"
    ZONE_4 = "Zone 4"
    X_POWER_3 = "X Power 3"
    K10 = "K10"
    K8 = "K8"
    ARISTO_2 = "Aristo 2"
    X4_PLUA = "X4+"
    V30 = "V30"
    Q6 = "Q6"
    Q_PAD_IV_80_FHD = "Q Pad IV 8.0 FHD"
    X_VENTURE = "X venture"
    G6 = "G6"
    X_POWER2 = "X power2"
    STYLO_3_PLUS = "Stylo 3 Plus"
    STYLUS_3 = "Stylus 3"
    HARMONY = "Harmony"
    K7 = "K7"
    K4 = "K4"
    K3 = "K3"


# Jan 2017-May 2020 HTC Phones
class HTC(Enum):
    U_ULTRA = "U Ultra"
    U_PLAY = "U Play"
    U11 = "U11"
    U11_PLUS = "U11+"
    U12_PLUS = "U12+"
    U12_LIFE = "U12 Life"


# Jan 2017-May 2020 Alcatel Phones
class Alcatel(Enum):
    ALCATEL_3L = "3L"
    ALCATEL_1S = "1S"
    ALCATEL_1V = "1V"
    ALCATEL_1B = "1B"
    ALCATEL_3V = "3v"
    ALCATEL_V = "v"
    ALCATEL_3T_8 = "3T 8"
    ALCATEL_3T_10 = "3T 10"
    ALCATEL_3 = "3"
    ALCATEL_1X = "1x"
    ALCATEL_1C = "1c"
    ALCATEL_1 = "1"
    ALCATEL_TETRA = "Tetra"
    ALCATEL_7 = "7"
    ALCATEL_5V = "5v"
    ALCATEL_5 = "5"
    ALCATEL_3X = "3x"
    ALCATEL_3C = "3c"
    ALCATEL_3088 = "3088"
    ALCATEL_1T_10 = "1T 10"
    ALCATEL_1T_7 = "1T 7"
    ALCATEL_IDOL_5S = "Idol 5s"
    ALCATEL_IDOL_5 = "Idol 5"
    ALCATEL_A7_XL = "A7 XL"
    ALCATEL_A7 = "A7"
    ALCATEL_U5_HD = "U5 HD"
    ALCATEL_PULSEMIX = "Pulsemix"
    ALCATEL_FLASH = "Flash"
    ALCATEL_U5 = "U5"
    ALCATEL_A5_LED = "A5 LED"
    ALCATEL_A3 = "A3"
    ALCATEL_A3_XL = "A3 XL"


# Jan 2017-May 2020 Vodafone Phones
class Vodafone(Enum):
    SMART_V10 = "Smart V10"
    SMART_N10 = "Smart N10"
    SMART_E9 = "Smart E9"
    SMART_X9 = "Smart X9"
    SMART_N9 = "Smart N9"
    SMART_N9_LITE = "Smart N9 lite"
    SMART_E8 = "Smart E8"
    SMART_V8 = "Smart V8"
    SMART_N8 = "Smart N8"


enum_to_manufacturer = {
    DeviceManufacturer.APPLE: list(Apple),
    DeviceManufacturer.SAMSUNG: list(Samsung),
    DeviceManufacturer.HUAWEI: list(Huawei),
    DeviceManufacturer.SONY: list(Sony),
    DeviceManufacturer.MOTOROLA: list(Motorola),
    DeviceManufacturer.GOOGLE: list(Google),
    DeviceManufacturer.ONEPLUS: list(OnePlus),
    DeviceManufacturer.XIAOMI: list(Xiaomi),
    DeviceManufacturer.NOKIA: list(Nokia),
    DeviceManufacturer.LENOVO: list(Lenovo),
    DeviceManufacturer.LG: list(LG),
    DeviceManufacturer.HTC: list(HTC),
    DeviceManufacturer.ALCATEL: list(HTC),
    DeviceManufacturer.VODAFONE: list(Vodafone)
}
