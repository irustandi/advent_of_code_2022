def main():
    with open("input") as f:
        input = f.readlines()

    chars = []
    for idx, c in enumerate(input[0].strip()):
        chars.append(c)
        if idx >= 13:
            char_set = set(chars)
            if len(char_set) == 14:
                print(idx)
                break

            chars.pop(0)


if __name__ == '__main__':
    main()