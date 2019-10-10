############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, 
                is_bestseller):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green',
                     True, True)
    # print(musk)
    musk.add_pairing('mint')

    casaba = MelonType('cas', 'Casaba', 2003, 'orange', False, False)
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')

    crenshaw = MelonType('cren', 'Crenshaw', 1996, 'green', False, False)
    crenshaw.add_pairing('proscuitto')

    yellow_watermelon = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow',
                                  False, True)
    yellow_watermelon.add_pairing('ice cream')

    all_melon_types.append(musk)
    all_melon_types.append(casaba)
    all_melon_types.append(crenshaw)
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # print(melon_types)

    for melon in melon_types:
        print(f"{melon.name} pairs with ")
        for pairing in melon.pairings:
            print("-", pairing)
    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # return 'musk': musk  
    # Fill in the rest
    melon_dictionary = {}

    for melon in melon_types:
        melon_dictionary[str(melon.code)] = melon

    # print(melon_dictionary)
    return melon_dictionary
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rate, color_rate, field, harvester):

        self.melon_type = melon_type
        self.shape_rate = shape_rate
        self.color_rate = color_rate
        self.field = field
        self.harvester = harvester

    def is_sellable(self, shape_rate, color_rate):

        if self.shape_rate > 5 and self.color_rate > 5 and self.field != 3:
            return True
        else:
            return False



def make_melons(melon_types):
    """Returns a list of Melon objects."""

    harvested_melons = []

    melon_dictionary = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melon_dictionary['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melon_dictionary['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melon_dictionary['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melon_dictionary['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melon_dictionary['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melon_dictionary['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melon_dictionary['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melon_dictionary['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melon_dictionary['yw'], 7, 10, 3, 'Sheila')

    harvested_melons.extend([melon_1, melon_2, melon_3, melon_4, 
                            melon_5, melon_6, melon_7, melon_8, melon_9])
    
    return harvested_melons

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable(melon.shape_rate, melon.color_rate):
            print(f'Harvested by {melon.harvester} from Field {melon.field} (CAN BE SOLD)')
        else:
            print(f'Harvested by {melon.harvester} from Field {melon.field} (NOT SELLABLE)')


melons = make_melon_types()
print_pairing_info(melons)
make_melon_type_lookup(melons)
get_sellability_report(make_melons(melons))