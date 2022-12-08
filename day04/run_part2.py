def main():
    with open("input") as f:
        input = f.readlines()

    print(len(input))
    total = 0

    for elem in input:
        ranges = elem.strip().split(",")
        range1 = [int(num) for num in ranges[0].split("-")]
        range2 = [int(num) for num in ranges[1].split("-")]

        if range1[0] < range2[0]:
            if range2[0] > range1[1]:
                total += 1
        elif range2[0] < range1[0]:
            if range1[0] > range2[1]:
                total += 1

    print(len(input) - total)

if __name__ == '__main__':
    main()
