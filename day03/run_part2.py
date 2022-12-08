def get_priority(c):
    c_ord = ord(c)
    ref_ord = ord('a') if c_ord > 90 else ord('A')

    distance = c_ord - ref_ord + 1
    if ref_ord < 90:
        distance += 26

    return distance


def main():
    with open("input") as f:
        input = f.readlines()

    print(len(input))
    score_total = 0

    for idx in range(0, len(input), 3):
        elem0 = set([c for c in input[idx].strip()])
        elem1 = set([c for c in input[idx+1].strip()])
        elem2 = set([c for c in input[idx+2].strip()])

        common_elem = list(set.intersection(
            set.intersection(elem0, elem1),
            elem2,
        ))[0]
        print(elem0)
        print(elem1)
        print(elem2)
        print(common_elem)

        score_total += get_priority(common_elem)

    print(score_total)
    

if __name__ == '__main__':
    main()