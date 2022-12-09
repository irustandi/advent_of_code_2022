def main():
    with open("input") as f:
        input = f.readlines()

    grids = []

    for elem in input:
        elem = elem.strip()
        grids.append([int(c) for c in elem])

    outer = 2 * len(grids) + 2 * (len(grids[0])-2)
    print(outer)

    visible_set = set()

    for row_idx in range(len(grids)):
        col_idx = 0
        height = -1
        while col_idx < len(grids[0]) - 1:
            if grids[row_idx][col_idx] > height:
                visible_set.add((row_idx, col_idx))
                height = grids[row_idx][col_idx]

            col_idx += 1

        col_idx = len(grids[0]) - 1
        height = -1

        while col_idx > 0:
            if grids[row_idx][col_idx] > height:
                visible_set.add((row_idx, col_idx))
                height = grids[row_idx][col_idx]

            col_idx -= 1

    for col_idx in range(len(grids[0])):
        row_idx = 0
        height = -1
        while row_idx < len(grids) - 1:
            if grids[row_idx][col_idx] > height:
                visible_set.add((row_idx, col_idx))
                height = grids[row_idx][col_idx]

            row_idx += 1

        row_idx = len(grids) - 1
        height = -1

        while row_idx > 0:
            if grids[row_idx][col_idx] > height:
                visible_set.add((row_idx, col_idx))
                height = grids[row_idx][col_idx]

            row_idx -= 1

    print(len(visible_set))

if __name__ == '__main__':
    main()
