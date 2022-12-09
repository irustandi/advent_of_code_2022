from collections import defaultdict

def main():
    with open("input") as f:
        input = f.readlines()

    keys = []
    dir_size_map = defaultdict(int)
    for elem in input:
        elem = elem.strip()
        if elem[0] == "$":
            inputs = elem.split(" ")
            if inputs[1] == "cd":
                if inputs[2] == "..":
                    keys.pop()
                else:
                    keys.append(inputs[2])
        else:
            inputs = elem.split(" ")
            if inputs[0] == "dir":
                continue
            else:
                size = int(inputs[0])

                for idx in range(1, len(keys)+1):
                    dir_size_map[" ".join(keys[:idx])] += size

    unused = 70000000 - dir_size_map["/"]
    to_free = 30000000 - unused
    print(unused)
    print(to_free)

    values = []

    for v in dir_size_map.values():
        if v >= to_free:
            values.append(v)

    print(min(values))


if __name__ == '__main__':
    main()
