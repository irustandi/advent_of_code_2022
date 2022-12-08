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

    for elem in input:
        elem = elem.strip()
        elem_len_half = int(len(elem) / 2)
        s1 = elem[:elem_len_half]
        s2 = elem[elem_len_half:]
        s1_set = set([c for c in s1])
        s2_set = set([c for c in s2])

        common_elem = list(set.intersection(s1_set, s2_set))[0]

        score_total += get_priority(common_elem)

    print(score_total)
    

if __name__ == '__main__':
    main()