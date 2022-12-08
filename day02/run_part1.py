SHAPE_SCORE_MAP = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

GAME_SCORE_MAP = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0,
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6,
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3,
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
        score_game = GAME_SCORE_MAP[codes[0]][codes[1]]

        score_total += score_shape + score_game

    print(score_total)


if __name__ == '__main__':
    main()
