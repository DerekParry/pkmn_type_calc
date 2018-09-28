NAME = 0
WEAK = 1
RESIST = 2
IMMUNE = 3

types = [
    # 0
    ('Bug', [5, 13, 4], [3, 8, 7], []),
    # 1
    ('Dragon', [1, 17, 9], [4, 14, 7, 2], []),
    # 2
    ('Electric', [8], [5, 16, 2], []),
    # 3
    ('Fighting', [5, 12, 17], [13, 0, 15], []),
    # 4
    ('Fire', [8, 13, 14], [0, 16, 4, 79, 17], []),
    # 5
    ('Flying', [13, 2, 9], [3, 0, 7], [8]),
    # 6
    ('Ghost', [6, 15], [11, 0], [10, 3]),
    # 7
    ('Grass', [5, 11, 0, 4, 9], [8, 14, 7, 2], []),
    # 8
    ('Ground', [14, 7, 9], [11, 13], [2]),
    # 9
    ('Ice', [3, 13, 16, 4], [9], []),
    # 10
    ('Normal', [3], [], [6]),
    # 11
    ('Poison', [8, 11], [3, 11, 0, 7, 17], []),
    # 12
    ('Psychic', [0, 6, 15], [3, 12], []),
    # 13
    ('Rock', [3, 8, 16, 14, 7], [10, 5, 11, 4], []),
    # 14
    ('Water', [7, 2], [16, 4, 14, 9], []),
    # 15
    ('Dark', [3, 0, 17], [6, 15], [12]),
    # 16
    ('Steel', [3, 8, 4], [10, 5, 13, 0, 16, 7, 12, 9, 1, 17], [11]),
    # 17
    ('Fairy', [11, 16], [3, 0, 15], [1]),
]


def combine(type1, type2):
    weak_x1 = []
    weak_x2 = []
    resist_x1 = []
    resist_x2 = []
    immune = []

    for w in type1[WEAK]:
        if w in type2[IMMUNE]:
            immune.append(w)
        elif w in type2[RESIST]:
            continue
        elif w in type2[WEAK]:
            weak_x2.append(w)

    for r in type1[RESIST]:
        if r in type2[IMMUNE]:
            immune.append(r)
        elif r in type2[RESIST]:
            resist_x2.append(r)
        elif r in type2[WEAK]:
            continue

    for i in type1[IMMUNE]:
        immune.append(i)

    weak_x1_str = ', '.join(set(weak_x1))
    weak_x2_str = ', '.join(set(weak_x2))
    resist_x1_str = ', '.join(set(resist_x1))
    resist_x2_str = ', '.join(set(resist_x2))
    immune_str = ', '.join(set(immune))

    print('------------------------')
    print(f'TYPE: {type1[NAME]} / {type2[NAME]}')
    print(f'=> WEAK x1: {weak_x1_str}')
    print(f'=> WEAK x2: {weak_x2_str}')
    print(f'=> RESIST x1: {resist_x1_str}')
    print(f'=> RESIST x2: {resist_x2_str}')
    print(f'=> IMMUNE: {immune_str}')
    print('------------------------')


def main():
    for t1 in types:
        for t2 in types:
            if t1[NAME] == t2[NAME]:
                continue
        combine(t1, t2)


if __name__ == '__main__':
    main()
