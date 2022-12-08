SHAPE_SCORE_MAP = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

GAME_SCORE_MAP = {
    "X": {
        "A": 3,
        "B": 1,
        "C": 2,
    },
    "Y": {
        "A": 1,
        "B": 2,
        "C": 3,
    },
    "Z": {
        "A": 2,
        "B": 3,
        "C": 1,
    }
}


def main():
    with open("input") as f:
        input = f.readlines()

    print(len(input))
    score_total = 0

    for elem in input:
        codes = elem.split()
        score_shape = SHAPE_SCORE_MAP[codes[1]]
        score_game = GAME_SCORE_MAP[codes[1]][codes[0]]

        score_total += score_shape + score_game

    print(score_total)


if __name__ == '__main__':
    main()
