from os import linesep

# enumeration for type properties
NAME = 0
WEAK = 1
RESIST = 2
IMMUNE = 3

# list of all types and their properties
# NOTE: indexing is strict and affects property sets - DO NOT reorganize list
types = [
    # 0
    ('Bug', {5, 13, 4}, {3, 8, 7}, set()),
    # 1
    ('Dragon', {1, 17, 9}, {4, 14, 7, 2}, set()),
    # 2
    ('Electric', {8}, {5, 16, 2}, set()),
    # 3
    ('Fighting', {5, 12, 17}, {13, 0, 15}, set()),
    # 4
    ('Fire', {8, 13, 14}, {0, 16, 4, 7, 9, 17}, set()),
    # 5
    ('Flying', {13, 2, 9}, {3, 0, 7}, {8}),
    # 6
    ('Ghost', {6, 15}, {11, 0}, {10, 3}),
    # 7
    ('Grass', {5, 11, 0, 4, 9}, {8, 14, 7, 2}, set()),
    # 8
    ('Ground', {14, 7, 9}, {11, 13}, {2}),
    # 9
    ('Ice', {3, 13, 16, 4}, {9}, set()),
    # 10
    ('Normal', {3}, set(), {6}),
    # 11
    ('Poison', {8, 11}, {3, 11, 0, 7, 17}, set()),
    # 12
    ('Psychic', {0, 6, 15}, {3, 12}, set()),
    # 13
    ('Rock', {3, 8, 16, 14, 7}, {10, 5, 11, 4}, set()),
    # 14
    ('Water', {7, 2}, {16, 4, 14, 9}, set()),
    # 15
    ('Dark', {3, 0, 17}, {6, 15}, {12}),
    # 16
    ('Steel', {3, 8, 4}, {10, 5, 13, 0, 16, 7, 12, 9, 1, 17}, {11}),
    # 17
    ('Fairy', {11, 16}, {3, 0, 15}, {1}),
]


# function to get a property set as a single string
def get_property_str(property_set):
    if not property_set:
        return '-'

    try:
        type_names = [types[t][NAME] for t in property_set]
        return ', '.join(type_names)
    except Exception:
        print(f'***ERROR PROCESSING SET {property_set} ***')


# define a class for a type combination
class TypeCombo:
    def __init__(self, t1, t2, w1, w2, r1, r2, i):
        self.type1 = t1
        self.type2 = t2
        self.weak_x1 = w1
        self.weak_x2 = w2
        self.resist_x1 = r1
        self.resist_x2 = r2
        self.immune = i

    def __str__(self):
        s = f'TYPE: {self.type1[NAME]} / {self.type2[NAME]}{linesep}'
        s += f'=> WEAK x1: {get_property_str(self.weak_x1)}{linesep}'
        s += f'=> WEAK x2: {get_property_str(self.weak_x2)}{linesep}'
        s += f'=> RESIST x1: {get_property_str(self.resist_x1)}{linesep}'
        s += f'=> RESIST x2: {get_property_str(self.resist_x2)}{linesep}'
        s += f'=> IMMUNE: {get_property_str(self.immune)}{linesep}'
        s += f'------------------------{linesep}'
        return s


# initialize a list of possible type combos
type_combos = []
# initialize a set of processed type combos
# new var so we can compare indexes instead of entire objects
processed_type_combos = []


# function to combine two types
# utilizes set operations to calculate new properties
def combine(type1, type2):
    # same type cannot be combined
    if type1[NAME] == type2[NAME]:
        return

    # calculate weak x2, resist x2, and immunities
    weak_x2 = type1[WEAK] & type2[WEAK]
    resist_x2 = type1[RESIST] & type2[RESIST]
    immune = type1[IMMUNE] | type2[IMMUNE]

    # initialize vars for reuse
    handled = weak_x2 | resist_x2 | immune
    weak_all = type1[WEAK] | type2[WEAK]
    resist_all = type1[RESIST] | type2[RESIST]

    # calculate weak x1 and resist x1
    weak_x1 = weak_all - resist_all - handled
    resist_x1 = resist_all - weak_all - handled

    # create and return a new TypeCombo
    return TypeCombo(type1, type2, set(weak_x1), set(weak_x2),
                     set(resist_x1), set(resist_x2), set(immune))


def main():
    # determine static length
    length = len(types)
    # loop over type combos
    for i1 in range(0, length):
        for i2 in range(0, length):
            # if types are the same, skip
            if i1 == i2:
                continue
            # initialize a set of indexes of the current combo
            combo_indexes = {i1, i2}
            # check if combo was already processed
            if combo_indexes not in processed_type_combos:
                # if not, combine types
                new_type = combine(types[i1], types[i2])
                # add new type to global list
                type_combos.append(new_type)
                # add index set to the list of processed combos
                processed_type_combos.append(combo_indexes)

    # print results
    [print(t) for t in type_combos]


if __name__ == '__main__':
    main()
