def main():
    with open("input") as f:
        input = f.readlines()

    print(len(input))
    total = 0

    for elem in input:
        ranges = elem.strip().split(",")
        range1 = [int(num) for num in ranges[0].split("-")]
        range2 = [int(num) for num in ranges[1].split("-")]

        if (range1[0] >= range2[0] and range1[1] <= range2[1]) or (range1[0] <= range2[0] and range1[1] >= range2[1]):
            print(elem)
            total += 1

    print(total)

if __name__ == '__main__':
    main()
