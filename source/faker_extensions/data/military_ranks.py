from enum import Enum


class MilitaryService(Enum):
    ROYAL_NAVY = "RN"
    ROYAL_MARINES = "RM"
    BRITISH_ARMY = "ARMY"
    ROYAL_AIR_FORCE = "RAF"


military_rank_distributions = {
    MilitaryService.ROYAL_NAVY: {
        # Distributions of ranks are provided combined for Navy/Marines, so appear identical for each NATO rank

        # The combined Royal Navy/Marines data includes OR-3 weightings. OR-3 does not exist in the Royal Navy
        # So the total weightings are short of 100%

        # Officers (21.0% of total Royal Navy)
        ("OF-9", "Admiral"): 0.00029256875 * 0.21,
        ("OF-8", "Vice-Admiral"): 0.01 * 0.21,
        ("OF-7", "Rear-Admiral"): 0.03 * 0.21,
        ("OF-6", "Commodore"): 0.012 * 0.21,
        ("OF-5", "Captain"): 0.038 * 0.21,
        ("OF-4", "Commander"): 0.154 * 0.21,
        ("OF-3", "Lieutenant-Commander"): 0.285 * 0.21,
        ("OF-2", "Lieutenant"): 0.334 * 0.21,
        # OF-1 and OF(D) are provided as a single value (17.1%), so I have split this (5.7% each)
        ("OF-1", "Sub-Lieutenant"): 0.057 * 0.21,
        ("OF-1", "Midshipman"): 0.057 * 0.21,
        ("OF(D)", "Officer Cadet"): 0.057 * 0.21,
        # Other Ranks (79.0% of total Royal Navy)
        ("OR-9", "Warrant Officer 1"): 0.037 * 0.79,
        ("OR-8", "Warrant Officer 2"): 0.013 * 0.79,
        ("OR-7", "Chief Petty Officer"): 0.112 * 0.79,
        ("OR-6", "Petty Officer"): 0.149 * 0.79,
        ("OR-4", "Leading Hand"): 0.232 * 0.79,
        ("OR-2", "Able Seaman"): 0.432 * 0.79
    },

    MilitaryService.ROYAL_MARINES: {
        # Distributions of ranks are provided combined for Navy/Marines, so appear identical for each NATO rank
        # As OR-3 only appears for Royal Marines, but comes from combined figures, it will be underrepresented.

        # Officers (21.0% of total)
        ("OF-9", "General"): 0.00029256875 * 0.21,
        ("OF-8", "Lieutenant-General"): 0.01 * 0.21,
        ("OF-7", "Major-General"): 0.03 * 0.21,
        ("OF-6", "Brigadier"): 0.012 * 0.21,
        ("OF-5", "Colonel"): 0.038 * 0.21,
        ("OF-4", "Lieutenant-Colonel"): 0.154 * 0.21,
        ("OF-3", "Major"): 0.285 * 0.21,
        ("OF-2", "Captain"): 0.334 * 0.21,
        # OF-1 and OF(D) are provided as a single value (17.1%), so I have split this (5.7% each)
        ("OF-1", "Lieutenant"): 0.057 * 0.21,
        ("OF-1", "2nd Lieutenant"): 0.057 * 0.21,
        ("OF(D)", "Officer Candidate"): 0.057 * 0.21,
        # Other Ranks (79.0% of total)
        ("OR-9", "Warrant Officer 1"): 0.037 * 0.79,
        ("OR-8", "Warrant Officer 2"): 0.013 * 0.79,
        ("OR-7", "Staff Sergeant"): 0.112 * 0.79,
        ("OR-6", "Sergeant"): 0.149 * 0.79,
        ("OR-4", "Corporal"): 0.232 * 0.79,
        ("OR-3", "Lance-Corporal"): 0.026 * 0.79,
        ("OF-2", "Private"): 0.432 * 0.79
    },
    MilitaryService.BRITISH_ARMY: {
        # Officers (16.3% of total)
        ("OF-9", "General"): 0.00031070374 * 0.163,
        ("OF-8", "Lieutenant-General"): 0.001 * 0.163,
        ("OF-7", "Major-General"): 0.003 * 0.163,
        ("OF-6", "Brigadier"): 0.012 * 0.163,
        ("OF-5", "Colonel"): 0.039 * 0.163,
        ("OF-4", "Lieutenant-Colonel"): 0.133 * 0.163,
        ("OF-3", "Major"): 0.318 * 0.163,
        ("OF-2", "Captain"): 0.313 * 0.163,
        # OF-1 and OF(D) are provided as a single value (17.9%), so I have split this (~5.96% each)
        ("OF-1", "Lieutenant"): 0.05966666666 * 0.163,
        ("OF-1", "2nd Lieutenant"): 0.05966666666 * 0.163,
        ("OF(D)", "Officer Candidate"): 0.05966666666 * 0.163,
        # Other Ranks (83.7% of total)
        ("OR-9", "Warrant Officer 1"): 0.02 * 0.837,
        ("OR-8", "Warrant Officer 2"): 0.055 * 0.837,
        ("OR-7", "Staff Sergeant"): 0.081 * 0.837,
        ("OR-6", "Sergeant"): 0.119 * 0.837,
        ("OR-4", "Corporal"): 0.183 * 0.837,
        ("OR-3", "Lance-Corporal"): 0.191 * 0.837,
        ("OF-2", "Private"): 0.35 * 0.837,
    },
    MilitaryService.ROYAL_AIR_FORCE: {
        # Officers (23.7% of total)
        ("OF-9", "Air Chief Marshal"): 0.0002567394 * 0.237,
        ("OF-8", "Air Marshal"): 0.001 * 0.237,
        ("OF-7", "Air Vice Marshal"): 0.003 * 0.237,
        ("OF-6", "Air Commodore"): 0.01 * 0.237,
        ("OF-5", "Group Captain"): 0.036 * 0.237,
        ("OF-4", "Wing Commander"): 0.128 * 0.237,
        ("OF-3", "Squadron Leader"): 0.261 * 0.237,
        ("OF-2", "Flight Lieutenant"): 0.379 * 0.237,
        # OF-1 and OF(D) are provided as a single value (18.1%), so I have split this (~6.03% each)
        ("OF-1", "Flying Officer"): 0.06033333333 * 0.237,
        ("OF-1", "Pilot Officer"): 0.06033333333 * 0.237,
        ("OF(D)", "Pilot Officer"): 0.06033333333 * 0.237,
        # Other Ranks (76.3% of total)
        ("OR-9", "Warrant Officer"): 0.037 * 0.763,
        # OR-7 is provided as a single value (9.3%), so I have split this (4.65% each)
        ("OR-7", "Flight Sergeant"): 0.465 * 0.763,
        ("OR-7", "Chief Technician"): 0.465 * 0.763,
        ("OR-6", "Sergeant"): 0.187 * 0.763,
        ("OR-4", "Corporal"): 0.252 * 0.763,
        # OR-2 is provided as a single value (6%), so I have split this (2% each)
        ("OR-2", "Senior Aircraftman/woman technician"): 0.2 * 0.763,
        ("OR-2", "Senior Aircraftman/woman"): 0.2 * 0.763,
        ("OR-2", "Leading Aircraftman/woman"): 0.2 * 0.763,
        ("OR-1", "Aircraftman"): 0.426 * 0.763
    }
}
