import numpy as np
def main():
    with open("input") as f:
        input = f.readlines()

    grids = []

    for elem in input:
        elem = elem.strip()
        grids.append([int(c) for c in elem])

    grids_array = np.array(grids)
    print(grids_array.shape)

    scores_left = np.zeros_like(grids_array)
    scores_right = np.zeros_like(grids_array)
    scores_top = np.zeros_like(grids_array)
    scores_bot = np.zeros_like(grids_array)

    for row_idx in range(grids_array.shape[0]):
        for col_idx in range(grids_array.shape[1]):
            if col_idx > 0:
                col_idx_iter = col_idx - 1
                while col_idx_iter > 0:
                    if grids_array[row_idx][col_idx] <= grids_array[row_idx][col_idx_iter]:
                        break

                    col_idx_iter -= 1

                scores_left[row_idx][col_idx] = col_idx - col_idx_iter

        for col_idx in range(grids_array.shape[1], -1, -1):
            if col_idx < grids_array.shape[1] - 1:
                col_idx_iter = col_idx + 1
                while col_idx_iter < grids_array.shape[1] - 1:
                    if grids_array[row_idx][col_idx] <= grids_array[row_idx][col_idx_iter]:
                        break

                    col_idx_iter += 1

                scores_right[row_idx][col_idx] = col_idx_iter - col_idx

    for col_idx in range(grids_array.shape[1]):
        for row_idx in range(grids_array.shape[0]):
            if row_idx > 0:
                row_idx_iter = row_idx - 1
                while row_idx_iter > 0:
                    if grids_array[row_idx][col_idx] <= grids_array[row_idx_iter][col_idx]:
                        break

                    row_idx_iter -= 1

                scores_top[row_idx][col_idx] = row_idx - row_idx_iter

        for row_idx in range(grids_array.shape[0], -1, -1):
            if row_idx < grids_array.shape[0] - 1:
                row_idx_iter = row_idx + 1
                while row_idx_iter < grids_array.shape[0] - 1:
                    if grids_array[row_idx][col_idx] <= grids_array[row_idx_iter][col_idx]:
                        break

                    row_idx_iter += 1

                scores_bot[row_idx][col_idx] = row_idx_iter - row_idx

    scores = scores_left * scores_right * scores_top * scores_bot
    print(scores_left)
    print(scores_right)
    print(scores_top)
    print(scores_bot)
    print(scores)

    print(np.max(scores))

if __name__ == '__main__':
    main()
